FROM python:3.9-slim

WORKDIR /app

COPY server.py /app/

RUN pip install --no-cache-dir --disable-pip-version-check --progress-bar off flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]