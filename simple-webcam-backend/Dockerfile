FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/

# Set PYTHONPATH to include /app/src
ENV PYTHONPATH=/app/src

# Make device handling scripts executable and add symlinks
RUN chmod +x /app/src/on_device_add.py && \
    chmod +x /app/src/on_device_remove.py
RUN ln -s /app/src/on_device_add.py /on_device_add && \
    ln -s /app/src/on_device_remove.py /on_device_remove

EXPOSE 50052

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "50052"]