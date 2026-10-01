# syntax=docker/dockerfile:1
FROM python:3.12-slim AS pybuild
WORKDIR /app
COPY *.py ./
COPY build_extensions.py ./
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir 'Cython==3.3.0' setuptools
RUN python build_extensions.py build_ext --inplace \
    && strip --strip-unneeded ./*.so

FROM python:3.12-slim
ARG TARGETARCH
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 DATA_DIR=/data ANYTLS_PORT=8443
COPY requirements.txt ./
COPY assets/ assets/
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=pybuild /app/*.so ./
COPY --chmod=755 bin/anytls-gateway-linux-${TARGETARCH} bin/anytls-gateway
EXPOSE 8000 8443
CMD ["python", "-c", "import main, uvicorn; uvicorn.run(main.app, host='0.0.0.0', port=main.CONFIG['port'], log_level='info', workers=1)"]
