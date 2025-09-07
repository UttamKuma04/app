FROM python:3.13-slim

# Install Chrome + Chromedriver
RUN apt-get update && apt-get install -y wget gnupg unzip chromium chromium-driver && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Run Streamlit (disable telemetry prompt, bind to Render's $PORT)
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]
