from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
PRICE_FILE=os.path.join(BASE_DIR,"current_price.txt")


URL=f'https://api.telegram.org/bot{os.getenv("TELEGRAM_TOKEN")}/sendMessage'


def send_to_telegram(message):
    try:
        response2 = requests.post(URL, json={'chat_id': os.getenv("CHAT_ID"), 'text': message})
        print(response2.text)
    except Exception as e:
        print(e)


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.binary_location = "/usr/bin/chromium-browser" 
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")

driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)
driver.get("https://gieldakaliska.pl/notowania")

price =driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/table/tbody/tr[116]/td[5]").text
driver.quit()




if not os.path.isfile('./current_price.txt'):
    with open(PRICE_FILE,mode='w') as file:
        file.write(price)
        send_to_telegram(f"Ogorek gruntowy Kalisz cena: {price} zl")
else:
    with open(PRICE_FILE,mode='r') as file:
        if file.read() != price:
            with open('./current_price.txt', mode='w') as f:
                f.write(price)
                send_to_telegram(f"Ogorek gruntowy Kalisz cena: {price} zl")