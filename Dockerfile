FROM python:3.10
WORKDIR /app
COPY . /app
# RUN pip install --no-cache-dir sqlite3
CMD ["python", "main.py"]