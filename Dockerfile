FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# TODO: Copy/install dependencies in a cache-friendly order.
# TODO: Copy application source.
# TODO: Add the correct startup command.
  