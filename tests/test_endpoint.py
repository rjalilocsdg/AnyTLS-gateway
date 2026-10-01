"""Public endpoint validation, subscription generation and persisted overrides."""
import asyncio
import base64
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class EndpointTest(unittest.TestCase):
    def test_endpoint_configuration(self):
        script = r'''
import asyncio, base64, os
import httpx
import main
from anytls_bridge import endpoint_config
async def run():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=main.app), base_url="http://test") as client:
        assert (await client.patch('/api/anytls', json={'endpoint':'example.com:443'})).status_code == 401
        assert (await client.post('/api/login', json={'password':'endpoint-test'})).status_code == 200
        await main.ensure_default_link()
        links = (await client.get('/api/links')).json()['links']
        uid = links[0]['uuid']
        assert links[0]['vless_link'] == ''
        assert (await client.get('/sub/'+uid)).status_code == 503
        for invalid in ['http://example.com:443', 'example.com', 'example.com:0', 'example.com:65536', 'user@example.com:443', 'a b:443', 'example.com:443/path', 5]:
            assert (await client.patch('/api/anytls', json={'endpoint':invalid})).status_code == 400, invalid
        response = await client.patch('/api/anytls', json={'endpoint':'altaria.proxy.rlwy.net:30321'})
        assert response.status_code == 200, response.text
        assert response.json()['source'] == 'saved'
        uri = (await client.get('/api/links')).json()['links'][0]['vless_link']
        assert '@altaria.proxy.rlwy.net:30321/' in uri, uri
        assert 'sni=altaria.proxy.rlwy.net' in uri
        assert base64.b64decode((await client.get('/sub/'+uid)).text).decode() == uri
        main.ANYTLS_SETTINGS.clear()
        await main.load_state()
        assert endpoint_config()['host'] == 'altaria.proxy.rlwy.net'
        assert endpoint_config()['port'] == 30321
        os.environ.update(RAILWAY_TCP_PROXY_DOMAIN='automatic.proxy.rlwy.net', RAILWAY_TCP_PROXY_PORT='12345')
        assert endpoint_config()['source'] == 'saved'
        response = await client.patch('/api/anytls', json={'endpoint':''})
        assert response.json()['host'] == 'automatic.proxy.rlwy.net'
        assert response.json()['port'] == 12345
        response = await client.patch('/api/anytls', json={'endpoint':'[2001:db8::1]:443'})
        assert response.status_code == 200
        assert '@[2001:db8::1]:443/' in (await client.get('/api/links')).json()['links'][0]['vless_link']
asyncio.run(run())
'''
        with tempfile.TemporaryDirectory() as directory:
            env = dict(os.environ, DATA_DIR=directory, ANYTLS_ENABLED='0', ADMIN_PASSWORD='endpoint-test')
            for key in ('ANYTLS_PUBLIC_HOST','ANYTLS_PUBLIC_PORT','RAILWAY_TCP_PROXY_DOMAIN','RAILWAY_TCP_PROXY_PORT'):
                env.pop(key, None)
            result = subprocess.run([sys.executable, '-c', script], cwd=Path(__file__).resolve().parent.parent,
                                    env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
