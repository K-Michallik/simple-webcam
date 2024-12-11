FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN ln -s /src/on_device_add.py /on_device_add

COPY src/ .

EXPOSE 50052

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "50052"]