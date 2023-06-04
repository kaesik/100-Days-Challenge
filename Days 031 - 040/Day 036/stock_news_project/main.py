import requests as rq
from twilio.rest import Client


# ----- INSTRUCTIONS ----- #

## STEP 1: Use https://www.alphavantage.com
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


# ----- CONSTANTS ----- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "L57RF7E5ANXGTS3X"
NEWS_API_KEY = "27ad8cb46a61410cbfe562c1d596a052"

SID = "AC4840665656d8ca24abe7c133d4036e60"
TOKEN = "c5bacae9f9ffe1f8d4b08d6a91100a48"


# ----- VARIABLES ----- #
parameters_stock = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
}

parameters_news = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}


# ----- FUNCTIONS ----- #
def get_stock(param):
    response = rq.get("https://www.alphavantage.co/query", params=param)
    response.raise_for_status()
    data = response.json()
    today_key = list(data["Time Series (60min)"])[0]
    yesterday_key = list(data["Time Series (60min)"])[16]
    today_close = float(data["Time Series (60min)"][today_key]["4. close"])
    yesterday_close = float(data["Time Series (60min)"][yesterday_key]["4. close"])
    percentage = round(((today_close - yesterday_close)/today_close)*100, 2)
    return percentage


def get_news(param):
    response = rq.get("https://newsapi.org/v2/everything", params=param)
    response.raise_for_status()
    data = response.json()
    articles = data["articles"][:3]
    title1, source1, url1 = articles[0]["title"], articles[0]["source"]["name"], articles[0]["url"]
    title2, source2, url2 = articles[1]["title"], articles[1]["source"]["name"], articles[1]["url"]
    title3, source3, url3 = articles[2]["title"], articles[2]["source"]["name"], articles[2]["url"]
    news = f"Title: '{title1}'\n" \
           f"Source: {source1} ➡ {url1}\n\n" \
           f"Title: '{title2}'\n" \
           f"Source: {source2} ➡ {url2}\n\n" \
           f"Title: '{title3}'\n" \
           f"Source: {source3} ➡ {url3}\n"
    return news


# ----- CODE ----- #
stock = get_stock(parameters_stock)
news = get_news(parameters_news)
text = f"🔹{stock}"
sms = f"{STOCK}: {text}\n\n{news}"

try:
    if stock < -5:
        text = f"🔻{stock}"
    elif stock > 5:
        text = f"🔺+{stock}"
finally:
    client = Client(SID, TOKEN)
    message = client.messages.create(
        body=sms,
        from_="+13613104234",
        to="+48695225397"
    )