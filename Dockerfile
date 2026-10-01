# syntax=docker/dockerfile:1
FROM python:3.12-slim
ARG TARGETARCH
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 DATA_DIR=/data ANYTLS_PORT=8443
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py ./
COPY --chmod=755 bin/anytls-gateway-linux-${TARGETARCH} bin/anytls-gateway
EXPOSE 8000 8443
CMD ["python", "main.py"]
