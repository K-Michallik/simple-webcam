FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
RUN chmod +x /app/src/on_device_add.py
RUN ln -s /app/src/on_device_add.py /on_device_add

EXPOSE 50052

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "50052"]