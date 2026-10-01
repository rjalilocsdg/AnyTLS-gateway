The native transport engine uses the official AnyTLS implementation and the
GPL-3.0-or-later sing library. Its corresponding source, vendored dependencies,
and license notices are provided in `native-source.tar.gz`.

Rebuild with Go 1.24 or later:

```sh
tar -xzf native-source.tar.gz
cd native
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -mod=vendor -trimpath -ldflags='-s -w' -o ../anytls-gateway .
```

Use `GOARCH=arm64` for the other distributed Linux binary.
The Python dashboard communicates with the engine through a Unix socket.
