# CFM Gateway

Deployable AnyTLS server with the CFM dashboard, subscription groups,
Telegram management bot, per-user passwords, traffic quotas, expiry, speed
limits, and live traffic statistics. VLESS/WebSocket and XHTTP remain available.

The transport uses the [official AnyTLS session engine](https://github.com/anytls/anytls-go),
pinned to commit `fd6167acd6d73b9fa3e607659951847fbc9e6c50`. It supports AnyTLS
v1/v2 sessions, padding negotiation, multiple streams, TCP, and UDP-over-TCP.
Each configuration's UUID is its AnyTLS password. Native code is compiled; the
Docker image ships encrypted Python 3.12 bytecode.

## CFM interface and distribution

CFM branding appears on the login, dashboard, and public subscription pages.
The interface uses a charcoal and teal palette, a vector CFM logo, responsive
navigation, visible keyboard focus, and light/dark dashboard themes. Icons are
served locally; the bundled Tabler font license is in `assets/TABLER-LICENSE`.

The seven Python modules are compiled with Python 3.12, with docstrings removed,
then marshaled and compressed. Each payload is encrypted with AES-256-GCM using
`CFM_ENCRYPTION_KEY`, then stored as shuffled Base85 chunks. Set that variable in
Railway to the 64-character hex key provided with this release. It is needed at
runtime; the already-encrypted repository can be built without the key. Docker
compiles the loader modules into stripped Cython extensions and omits their
Python wrappers from the final image. This makes static inspection harder; the
application bytecode still exists in process memory at runtime. Keep the key out
of the repository. The Dockerfile pins Python 3.12. Compiled native binaries and
their license/source archive are retained.

## Deploy on Railway

1. Deploy this repository as a new service. Railway builds the Dockerfile.
2. Add `ADMIN_PASSWORD` with a strong password. Leave `ANYTLS_PORT=8443`.
3. Attach a persistent volume at `/data` for users, usage, secrets, and TLS keys.
4. Generate an HTTPS domain for the dashboard, targeting the `PORT` environment
   variable (8000 if you set `PORT=8000`). Open `/dashboard` and log in.
5. Add a **TCP Proxy targeting internal port 8443** in Networking. This is
   required for AnyTLS; an ordinary HTTPS domain cannot carry this protocol.
6. Redeploy after creating the TCP Proxy so its domain and external port are
   available to the application. Create a configuration with protocol **AnyTLS**
   and copy its `anytls://` link or subscription from the dashboard.

The AnyTLS endpoint detects `RAILWAY_TCP_PROXY_DOMAIN` and
`RAILWAY_TCP_PROXY_PORT` on each request. Its external port can differ from 8443.
If the proxy variables are unavailable, open **Settings → AnyTLS · TCP Proxy**,
enter the public `hostname:port` from Railway, and save. The current Railway TCP proxy address always takes priority, so new projects
automatically generate links with their own hostname and external port. The saved
address is used only if Railway and explicit endpoint variables are unavailable.
Use “automatic settings” to clear the saved address. This setting persists in `/data`.
Until an endpoint is configured, the panel does not generate a localhost link.

The HTTPS dashboard and raw AnyTLS TCP listener share one service.
Use one replica: this implementation stores users and quotas locally.

[Railway TCP Proxy documentation](https://docs.railway.com/networking/tcp-proxy)
and [network variables](https://docs.railway.com/variables/reference).

## TLS certificates

For immediate deployment, the service generates and persists a self-signed TLS
certificate. Generated links explicitly include `insecure=1`, so clients skip
certificate verification in this mode. This encrypts traffic but does not
protect against a TLS impersonation attack.

For verified TLS, point `ANYTLS_TLS_CERT` and `ANYTLS_TLS_KEY` to your PEM
certificate and private key, set `ANYTLS_SNI` to the certificate hostname, and
set `ANYTLS_INSECURE=0`. Restart after renewing the certificate. A custom TCP
hostname must be DNS-only if using Cloudflare. Railway's automatic HTTPS
certificate belongs to its HTTP edge; it is not the raw TCP listener's certificate.

Alternatively, import `/data/anytls.crt` as a trusted certificate in a client
that supports custom CAs and set `ANYTLS_INSECURE=0`. It is available to logged-in
admins at `/api/anytls/certificate`. Standard AnyTLS share links cannot embed it.

## User limits

Uploaded and downloaded stream bytes share each user's quota and speed bucket.
UDP-over-TCP framing is included; TLS/session padding is excluded. A stream is
closed when its configuration is disabled, expired, deleted, or out of quota.
Usage is saved every three seconds and during graceful shutdown; abrupt failure
can lose the most recent unsaved usage.

IP limits use the peer address visible to the listener. Railway's TCP Proxy
does not expose the original client IP, so these limits cannot distinguish
users behind that proxy. Deploy directly on a VPS for real client IP limits.

## Environment

| Variable | Default | Purpose |
|---|---|---|
| `ADMIN_PASSWORD` | `admin` | Dashboard login; set before public deployment |
| `CFM_ENCRYPTION_KEY` | required | 64 hexadecimal characters; keep it as a private Railway variable |
| `PORT` | `8000` | HTTP dashboard listener |
| `DATA_DIR` | `/data` | Persistent state and generated TLS files |
| `ANYTLS_PORT` | `8443` | Internal TLS/TCP listener |
| `ANYTLS_PUBLIC_HOST` | Railway TCP domain or `localhost` | Override client hostname |
| `ANYTLS_PUBLIC_PORT` | Railway TCP port or `ANYTLS_PORT` | Override client port |
| `ANYTLS_SNI` | AnyTLS public hostname | Certificate hostname for clients |
| `ANYTLS_TLS_CERT` / `ANYTLS_TLS_KEY` | generated certificate | PEM certificate paths |
| `ANYTLS_INSECURE` | `1` for generated cert; `0` for supplied cert | Client verification flag |
| `ANYTLS_PADDING_SCHEME` | upstream default | Optional padding scheme file |
| `TELEGRAM_BOT_TOKEN` | unset | Optional Telegram bot |
| `TELEGRAM_ADMIN_IDS` | unset | Comma-separated authorized admin IDs |

Fingerprint, ALPN, and per-link port controls apply to VLESS/XHTTP. AnyTLS uses
the service-wide public endpoint and client TLS preferences.

## Local development / VPS

Requires Python 3.12 and Go 1.24 or later:

```sh
cd native
go build -trimpath -ldflags='-s -w' -o ../bin/anytls-gateway .
cd ..
python3 -m pip install -r requirements.txt
DATA_DIR=./data ANYTLS_PUBLIC_HOST=your.domain ADMIN_PASSWORD=change-me python3 main.py
```

For a VPS, expose TCP port 8443 and put the dashboard behind an HTTPS reverse
proxy. For Docker, publish the dashboard and AnyTLS ports and mount `/data`.
Clients include sing-box, mihomo, and applications supporting the AnyTLS URI.

Based on [rjalilocsdg/NewYork](https://github.com/rjalilocsdg/NewYork).
