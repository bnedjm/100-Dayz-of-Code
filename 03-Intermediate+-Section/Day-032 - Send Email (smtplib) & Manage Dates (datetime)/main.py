from smtplib import *
from datetime import *
from random import *

EMAIL_SENDER = "tester.py99@gmail.com"
APP_PASSWORD = "juslsfmekfbyvpnn"

motiv_oclock = datetime(day=29, month=11, year=2022)
weekday = datetime.now().weekday()

if weekday == motiv_oclock.weekday():
    try:
        with open("quotes.txt", "r") as file:
            data = file.readlines()

    except FileNotFoundError:
        print("File Not Found!")

    else:
        subject = "Motivation O'Clock"
        quote = choice(data)

        with SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=EMAIL_SENDER, password=APP_PASSWORD)
            connect.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=EMAIL_SENDER,
                msg=f"Subject: {subject}\n\n"
                    f"{quote}"
            )
