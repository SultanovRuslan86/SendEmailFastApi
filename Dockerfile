FROM python:3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

COPY .env /app/.env

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

