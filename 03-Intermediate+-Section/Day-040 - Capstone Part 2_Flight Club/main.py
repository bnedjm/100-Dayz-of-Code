import os
import requests

USER_ID = os.environ.get("USER_IDENTIFICATION")
TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")

SHEETY_ENDPOINT = f"https://api.sheety.co/{USER_ID}/flightDeals/users"

sheety_headers = {
    "Authorization": TOKEN,
}


def new_user():
    user_firstname = input("What's your first name?\t").title()
    user_lastname = input("What's your last name?\t").title()
    user_email_1 = ""
    user_email_2 = ""

    while not validate_email(user_email_1, user_email_2):
        user_email_1 = input("What's your email address?\t").lower()
        user_email_2 = input("Type your email address again?\t").lower()

    new_user = {
        "user": {
            "firstName": user_firstname,
            "lastName": user_lastname,
            "email": user_email_1,
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=new_user, headers=sheety_headers)
    response.raise_for_status()
    # print(response.text)

    print("Your email has been added to our database.\nWelcome to the Club!\n")


def validate_email(email, retyped_email):
    if email != "" and email == retyped_email:
        return True
    else:
        return False


print("Welcome to the Flight Club.\nWe find the best flight deals for you!")
retry = "yes"
while retry == "yes":
    new_user()
    retry = input("Do you want to enter another user? 'yes'/'no'\t").lower()
