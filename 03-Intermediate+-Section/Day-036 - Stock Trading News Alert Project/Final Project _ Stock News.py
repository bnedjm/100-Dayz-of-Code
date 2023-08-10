import os
import requests
from twilio.rest import Client

# Stock Information
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

# APIs' Keys
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# Twilio Account Information
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
MY_NUMBER = os.environ.get("MY_NUMBER")

# Private definitions
OPEN = "1. open"
CLOSE = "4. close"

# Parameters
STOCK_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    # "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

NEWS_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

# get stock data
response = requests.get(STOCK_ENDPOINT, params=STOCK_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# calculate the percentage change between yesterday's closing and the day before yesterday's closing
yesterday_idx = list(data.keys())[0]
before_yesterday_idx = list(data.keys())[1]
yesterday_close = float(data[yesterday_idx][CLOSE])
before_yesterday_close = float(data[before_yesterday_idx][CLOSE])

percentage_change = 100 * (yesterday_close - before_yesterday_close) / before_yesterday_close

# if the change is more than 5%, get stock news
if abs(percentage_change) >= 5:
    response = requests.get(NEWS_ENDPOINT, params=NEWS_params)
    response.raise_for_status()
    news = response.json()["articles"]

    # create a new list of the latest 3 articles and format them as needed
    latest_3_articles = news[:3]
    sign = "🔺" if percentage_change > 0 else "🔻"
    formatted_articles = [f"{COMPANY_NAME}: {sign}{round(percentage_change)}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in latest_3_articles]

    # send the articles in different SMS messages
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=article,
            from_="+15108801602",
            to=MY_NUMBER,
        )

        print(message.status)
