FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --progress-bar off flask gunicorn
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]