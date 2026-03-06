# Projet : Supervision de Production (API Python)

## 1. Comment lancer la solution
- Lancement : `docker-compose up --build -d`
- Arrêt : `docker-compose down`
- Accès API : `http://localhost:5000/api/data`
- Accès Grafana : `http://localhost:3000` (admin/admin)

## 2. Modèle de Supervision (SLI/SLO)
- [cite_start]**SLI 1 (Disponibilité)** : Ratio de succès HTTP (codes non-5xx)[cite: 31].
- [cite_start]**SLI 2 (Latence)** : Temps de réponse p95[cite: 31, 39].
- **SLO** : 99,5% de succès sur 30 jours. [cite_start]Justification : Un seuil standard pour garantir une haute disponibilité sans surcoût opérationnel excessif[cite: 32, 33].

## 3. Alerting Actionnable
- [cite_start]**API_High_Error_Rate** (Symptôme) : Déclenchée si le taux d'erreur dépasse 5%[cite: 52, 53].
- [cite_start]**Host_High_CPU_Usage** (Saturation) : Déclenchée si le CPU dépasse 85%[cite: 52, 54].
- [cite_start]**Service_Down** (Qualité) : Déclenchée si l'API est injoignable (up == 0)[cite: 52, 55].

## 4. Diagnostics (N2)
[cite_start]En cas d'alerte, utiliser le lien drilldown vers le dashboard secondaire ou la vue Explore pour analyser les métriques par endpoint[cite: 49, 50].