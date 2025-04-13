# 🥒 Kalisz Cucumber Price Tracker

A simple Python script that automatically checks the price of "Ogórek gruntowy" (field cucumber) from [gieldakaliska.pl](https://gieldakaliska.pl/notowania) and sends a notification to a Telegram bot if the price changes.

## 📌 What It Does

- Uses Selenium with Chromium in headless mode to scrape cucumber prices from a specific row in a table.
- Compares the current price to the last known price stored in a file (`current_price.txt`).
- Sends a Telegram message with the new price if it has changed.
- Runs automatically every 30 minutes using `cron` on a Raspberry Pi 5.

## 💡 Use Case

You want to be notified on Telegram when the market price for field cucumbers in Kalisz changes — without manually checking the website.

## 🧰 Technologies Used

- Python 3
- Selenium
- Chromium (headless mode)
- Telegram Bot API
- dotenv
- Raspberry Pi OS (tested on Raspberry Pi 5)

## 🛠 Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/kalisz-cucumber-tracker.git
cd kalisz-cucumber-tracker
