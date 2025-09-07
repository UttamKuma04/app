FROM python:3.13-slim

# Install Chrome + Chromedriver
RUN apt-get update && apt-get install -y wget gnupg unzip chromium chromium-driver && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Streamlit
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
