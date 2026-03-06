from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Counter, Histogram, Gauge
import time
import random

app = Flask(__name__)

# --- METRIQUES PROMETHEUS ---
# 1. Trafic & Erreurs (SLI Disponibilité)
HTTP_REQUESTS_TOTAL = Counter(
    'http_requests_total', 'Nombre total de requetes HTTP',
    ['method', 'endpoint', 'status']
)

# 2. Latence (SLI Performance - p95) 
HTTP_REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds', 'Latence des requetes en secondes',
    ['endpoint'],
    buckets=[0.1, 0.3, 0.5, 0.7, 1, 2, 5]
)

# 3. Saturation (Simulée pour l'exercice) 
APP_MEMORY_USAGE = Gauge('app_memory_usage_bytes', "Utilisation memoire simulee de l'application")

@app.route('/api/data')
def get_data():
    start_time = time.time()
    
    # Simulation d'un comportement de production
    time.sleep(random.uniform(0.05, 0.4)) # Latence normale
    
    status = 200
    # Simulation de 5% d'erreurs pour tester l'alerting [cite: 53]
    if random.random() < 0.05:
        status = 500
        
    # Enregistrement des métriques
    duration = time.time() - start_time
    HTTP_REQUESTS_TOTAL.labels(method='GET', endpoint='/api/data', status=status).inc()
    HTTP_REQUEST_LATENCY.labels(endpoint='/api/data').observe(duration)
    APP_MEMORY_USAGE.set(random.uniform(50000000, 100000000)) # ~50-100MB

    if status == 500:
        return jsonify({"error": "Internal Server Error"}), 500
    return jsonify({"status": "ok", "latency": duration})

if __name__ == "__main__":
    # Port 8000 pour les métriques, 5000 pour l'application [cite: 28, 29]
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)