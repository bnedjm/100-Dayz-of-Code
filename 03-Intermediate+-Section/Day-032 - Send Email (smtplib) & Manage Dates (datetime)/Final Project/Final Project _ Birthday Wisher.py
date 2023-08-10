from pandas import *
from datetime import *
from random import *
from smtplib import *

EMAIL_SENDER = "tester.py99@gmail.com"
APP_PASSWORD = "juslsfmekfbyvpnn"
PLACEHOLDER = "[NAME]"

# 1. Update the birthdays.csv

try:
    data = read_csv("birthdays.csv")

except FileNotFoundError:
    print("File Not Found! >> Data CSV.")

else:
    database = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
    print(database)
    # 2. Check if today matches a birthday in the birthdays.csv
    now = datetime.now()
    today = (now.month, now.day)

    if today in database:

        per = database[today]
        name = per["name"].title()
        email = per["email"]
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
        # person's actual name from birthdays.csv
        try:
            path = f"./letter_templates/letter_{randint(1, 3)}.txt"
            with open(path) as letter_file:
                letter = letter_file.read()
                letter = letter.replace(PLACEHOLDER, f"{name}")

        except FileNotFoundError:
            print("File Not Found! >> Letter Temps.")

        # 4. Send the letter generated in step 3 to that person's email address.
        else:
            subject = f"Happy Birthday {name}"
            with SMTP("smtp.gmail.com", port=587) as connect:
                connect.starttls()
                connect.login(user=EMAIL_SENDER, password=APP_PASSWORD)
                connect.sendmail(
                    from_addr=EMAIL_SENDER,
                    to_addrs=email,
                    msg=f"Subject: {subject}\n\n"
                        f"{letter}"
                )
