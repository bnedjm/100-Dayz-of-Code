import os
import string
import requests
from flight_data import FlightData
from pprint import pprint

API_KEY = os.environ.get("API_KEY")

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
LOCATIONS_ENDPOINT = f"{TEQUILA_ENDPOINT}/locations/query?"
SEARCH_ENDPOINT = f"{TEQUILA_ENDPOINT}/v2/search?"

tequila_headers = {
    "apikey": API_KEY,
}

FLIGHT_TYPE = "round"
RETURN_MIN_DATE = 7
RETURN_MAX_DATE = 28
STOPS = 0
CURRENCY = "PLN"
CHEAPEST = 1


class FlightSearch:

    def get_iata(self, city_name: string):
        search_params = {
            "term": city_name,
        }
        # GET REQUEST
        # search iata and return it
        response = requests.get(url=LOCATIONS_ENDPOINT, params=search_params, headers=tequila_headers)
        response.raise_for_status()
        city_iata = response.json()["locations"][0]["code"]
        # return the iataCode
        return city_iata

    def search_flights(self, fly_from, fly_to, date_from, date_to):
        search_params = {
            "flight_type": FLIGHT_TYPE,
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": RETURN_MIN_DATE,
            "nights_in_dst_to": RETURN_MAX_DATE,
            "max_stopovers": STOPS,
            "curr": CURRENCY,
            "one_for_city": CHEAPEST,
        }
        # GET REQUEST
        # search flights | TEQUILA API
        response = requests.get(url=SEARCH_ENDPOINT, params=search_params, headers=tequila_headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            search_params.update({
                "max_stopovers": 2,
            })
            response = requests.get(url=SEARCH_ENDPOINT, params=search_params, headers=tequila_headers)
            response.raise_for_status()
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight = FlightData(
                    departure_city=data["cityFrom"],
                    departure_airport_code=data["flyFrom"],
                    dest_city=data["cityTo"],
                    dest_airport_code=data["flyTo"],
                    outbound_date=data["route"][0]["utc_departure"].split("T")[0],
                    inbound_date=data["route"][3]["utc_departure"].split("T")[0],
                    lowestprice=data["price"],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                )

                return flight
        else:
            flight = FlightData(
                departure_city=data["cityFrom"],
                departure_airport_code=data["flyFrom"],
                dest_city=data["cityTo"],
                dest_airport_code=data["flyTo"],
                outbound_date=data["route"][0]["utc_departure"].split("T")[0],
                inbound_date=data["route"][1]["utc_departure"].split("T")[0],
                lowestprice=data["price"],
            )

            return flight
