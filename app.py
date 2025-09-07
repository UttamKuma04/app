import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

st.title("🔎 Webpage Title Extractor with Selenium")

url = st.text_input("Enter a URL", "https://www.irctc.co.in/nget/train-search")

if st.button("Get Title"):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    service = Service(log_output=None)  # silence chromedriver logs

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(3)
        title = driver.title
        st.success(f"Page Title: {title}")

        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)
        st.image(screenshot_path, caption="Webpage Screenshot", use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        driver.quit()
