import requests
from datetime import *
from smtplib import *
import time

MY_LAT = 52.525578
MY_LNG = 13.373325
EMAIL_SENDER = "tester.py99@gmail.com"
APP_PASSWORD = "juslsfmekfbyvpnn"


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if abs(iss_longitude - MY_LNG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True


def is_dark():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_time = datetime.now()
    current_hour = current_time.hour

    if sunset <= current_hour or current_hour <= sunrise:
        return True


# If the ISS is close to my current position
# and if it is currently dark
while True:
    if is_close() and is_dark():
        # Then email me to tell me to look up.
        subject = f"Look Up! ISS Is Visible."
        letter = "The ISS is above in the sky."
        with SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=EMAIL_SENDER, password=APP_PASSWORD)
            connect.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=EMAIL_SENDER,
                msg=f"Subject: {subject}\n\n"
                    f"{letter}"
            )
    time.sleep(60)
