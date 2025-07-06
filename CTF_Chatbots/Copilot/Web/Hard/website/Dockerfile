FROM python:3.10

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir --progress-bar off flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
