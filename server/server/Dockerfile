FROM python:3.12-slim

WORKDIR /app

# Dependencies eerst (cache-vriendelijk)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

# Niet als root draaien (least privilege)
RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /data && chown appuser:appuser /data
USER appuser

VOLUME ["/data"]
EXPOSE 8000

CMD ["python", "server.py"]
