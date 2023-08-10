import requests
import os
from smtplib import *
from bs4 import BeautifulSoup
from email.mime.text import MIMEText


EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

URL = "https://www.amazon.com/Logitech-Master-Wireless-Mouse-Rechargeable/dp/B071YZJ1G1/ref=sr_1_13?crid" \
      "=1CC3BNZCI48TE&keywords=logitech%2Bmouse&qid=1673442393&s=electronics&sprefix=logitech%2Bmous%2Celectronics" \
      "-intl-ship%2C223&sr=1-13&th=1 "

TARGET_PRICE = 77.17

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en,fr;q=0.9",
}
response = requests.get(URL, headers=headers)
response.raise_for_status()
amazon_website = response.text

soup = BeautifulSoup(amazon_website, "html.parser")

price = float(soup.select_one(selector="#corePriceDisplay_desktop_feature_div > "
                                       "div.a-section.a-spacing-none.aok-align-center > "
                                       "span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > "
                                       "span.a-offscreen "
                              ).getText().strip("$"))

title = soup.select_one(selector="#productTitle").getText()

if price <= TARGET_PRICE:
    # format the email
    body = f"Product: {title}\nCurrent price: {price}$\n\n{URL}"
    text_type = "html"
    msg = MIMEText(body.replace("\n", "<br>"), text_type, 'utf-8')
    msg['Subject'] = "Amazon Price Alert!"
    # SMTP send email
    with SMTP("smtp.gmail.com", port=587) as connect:
        connect.starttls()
        connect.login(user=EMAIL_SENDER, password=APP_PASSWORD)
        connect.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=EMAIL_RECEIVER,
            msg=msg.as_string(),
        )
