FROM python:3.11-slim

RUN apt update && apt install -y \
    netcat-openbsd \
    gcc \
    libpq-dev \
    && apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
