import os
import requests

USER_ID = os.environ.get("USER_IDENTIFICATION")
TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")

SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{USER_ID}/flightDeals/prices"
SHEETY_USERS_ENDPOINT = f"https://api.sheety.co/{USER_ID}/flightDeals/users"

sheety_headers = {
    "Authorization": TOKEN,
}


class DataManager:

    def __init__(self):
        self.dest_info = []
        self.cx_info = []

    def get_dest_info(self):
        # GET REQUEST
        # get info from Google sheet
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        self.dest_info = response.json()["prices"]
        return self.dest_info

    def update_dest_info_iata(self):
        # PUT REQUEST
        # update info in the Google sheet
        for dest in self.dest_info:
            SHEETY_PUT_ENDPOINT = f"{SHEETY_PRICES_ENDPOINT}/{dest['id']}"
            dest_update = {
                "price": {
                    "iataCode": dest["iataCode"],
                }
            }
            response = requests.put(url=SHEETY_PUT_ENDPOINT, json=dest_update, headers=sheety_headers)
            response.raise_for_status()

    def get_cx_info(self):
        # GET REQUEST
        # get info from Google sheet
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        self.cx_info = response.json()["users"]
        return self.cx_info
