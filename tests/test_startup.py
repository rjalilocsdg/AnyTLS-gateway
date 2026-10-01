"""Regression check for the same command used by the deployment Dockerfile."""

import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import URLError
from urllib.request import urlopen


class StartupTest(unittest.TestCase):
    def test_script_entrypoint_and_lifespan(self):
        root = Path(__file__).resolve().parent.parent
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            port = listener.getsockname()[1]
        with tempfile.TemporaryDirectory(prefix="gateway-startup-") as directory:
            env = dict(os.environ, PORT=str(port), DATA_DIR=directory,
                       ANYTLS_ENABLED="0", TELEGRAM_BOT_TOKEN="", PYTHONWARNINGS="default")
            log_path = Path(directory) / "startup.log"
            with log_path.open("wb") as log:
                process = subprocess.Popen([sys.executable, "main.py"], cwd=root, env=env,
                                           stdout=log, stderr=subprocess.STDOUT)
                try:
                    deadline = time.monotonic() + 15
                    while time.monotonic() < deadline:
                        if process.poll() is not None:
                            self.fail(log_path.read_text())
                        try:
                            with urlopen(f"http://127.0.0.1:{port}/health", timeout=0.5) as response:
                                self.assertEqual(json.load(response)["status"], "ok")
                            break
                        except (URLError, OSError):
                            time.sleep(0.1)
                    else:
                        self.fail("Server did not start: " + log_path.read_text())
                finally:
                    if process.poll() is None:
                        process.terminate()
                        try:
                            process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            process.kill()
                            process.wait()
                self.assertEqual(process.returncode, 0, log_path.read_text())
                output = log_path.read_text()
                self.assertIn("Application startup complete", output)
                self.assertIn("Application shutdown complete", output)
                self.assertNotIn("ImportError", output)
                self.assertNotIn("on_event is deprecated", output)


if __name__ == "__main__":
    unittest.main()
