# Elastic AI Demo

A demonstration project showcasing security incident detection and
AI-powered threat analysis using:

-   Elasticsearch
-   Kibana
-   Docker
-   Google Gemini (Generative AI API)

------------------------------------------------------------------------

## Overview

This project simulates real-world cloud security incidents and
demonstrates how:

1.  Logs are ingested into Elasticsearch\
2.  Threat patterns are detected\
3.  An AI agent analyzes suspicious activity\
4.  Risk insights are generated using Generative AI

------------------------------------------------------------------------

## Project Structure

elastic-ai-demo/ ├── README.md ├── requirements.txt ├──
docker-compose.yml ├── run_agent.py ├── agent/ │ ├── analyzer.py │ ├──
elastic_client.py │ └── ai_client.py ├── data_exfiltration.json ├──
iam_escalation.json ├── sa_key_leak.json ├── secret_breach.json └──
logs.json

------------------------------------------------------------------------

## Architecture

Security Logs → Elasticsearch → AI Agent → Gemini AI → Risk Insights ↓
Kibana

------------------------------------------------------------------------

## Prerequisites

-   Docker (v20+)
-   Docker Compose (v1.29+)
-   Python 3.8+
-   pip
-   Git

Optional: - Google Cloud Project - Google API Key

------------------------------------------------------------------------

## Installation

### 1. Clone Repository

git clone https://github.com/jitu028/elastic-ai-demo.git cd
elastic-ai-demo

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Configure Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_google_api_key ELASTICSEARCH_HOST=localhost
ELASTICSEARCH_PORT=9200 KIBANA_HOST=localhost KIBANA_PORT=5601

### 4. Start Services

docker-compose up -d

------------------------------------------------------------------------

## Quick Start

Verify Elasticsearch:

curl http://localhost:9200/\_cluster/health?pretty

Access Kibana:

http://localhost:5601

Load Sample Data:

curl -X POST "http://localhost:9200/\_bulk" -H 'Content-Type:
application/json' -d @data_exfiltration.json

Run AI Agent:

python run_agent.py

------------------------------------------------------------------------

## Security Scenarios

1.  Data Exfiltration\
2.  IAM Privilege Escalation\
3.  Service Account Key Leak\
4.  Secret / Credential Exposure

------------------------------------------------------------------------

## Docker Configuration

Elasticsearch: - Version: 8.13.4 - Port: 9200 - JVM Heap: 1GB

To increase memory:

environment: - ES_JAVA_OPTS=-Xms2g -Xmx2g

------------------------------------------------------------------------

## Troubleshooting

Elasticsearch logs:

docker-compose logs elasticsearch

Restart services:

docker-compose restart elasticsearch

Reinstall dependencies:

pip install --upgrade -r requirements.txt

------------------------------------------------------------------------

## Production Notes

This is a demo project. For production: - Enable Elasticsearch
security - Use HTTPS - Protect API keys - Configure authentication

------------------------------------------------------------------------

## License

MIT License

Maintainer: @jitu028 Last Updated: February 22, 2026
