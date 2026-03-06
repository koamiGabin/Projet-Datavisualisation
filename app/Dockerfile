
FROM python:3.9-slim
WORKDIR /app
# Copie d'abord les requirements pour optimiser le cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copie le reste du code
COPY . .
EXPOSE 5000 8000
CMD ["python", "main.py"]