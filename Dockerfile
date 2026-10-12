FROM python:3.12-slim
WORKDIR /app

copy requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

copy . .

expose 8000

cmd ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# TODO: Copy/install dependencies in a cache-friendly order.
# TODO: Copy application source.
# TODO: Add the correct startup command.
