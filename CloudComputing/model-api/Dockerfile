FROM python:3.10

# Tambahkan library yang diperlukan
RUN apt-get update && apt-get install -y libgomp1

# Copy aplikasi Anda ke dalam container
COPY . /app
WORKDIR /app

# Install dependencies Python
RUN pip install -r requirements.txt

# Tetapkan entrypoint ke aplikasi Anda
CMD ["python", "main.py"]
