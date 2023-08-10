from datetime import *
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_dest_data = data_manager.get_dest_info()
sheet_cx_data = data_manager.get_cx_info()
flight_search = FlightSearch()
notification = NotificationManager()

update_needed = False
for dest in sheet_dest_data:
    if dest["iataCode"] == "":
        dest["iataCode"] = flight_search.get_iata(dest["city"])
        update_needed = True

if update_needed:
    data_manager.dest_info = sheet_dest_data
    data_manager.update_dest_info_iata()

DEPARTURE_IATA = "POZ"
tomorrow = datetime.now() + timedelta(days=1)
six_months_later = tomorrow + timedelta(days=180)
emails = [cx_data["email"] for cx_data in sheet_cx_data]

for dest in sheet_dest_data:
    # search flights
    flight = flight_search.search_flights(
        fly_from=DEPARTURE_IATA,
        fly_to=dest["iataCode"],
        date_from=tomorrow,
        date_to=six_months_later
    )

    # send notification
    if flight is None:
        continue

    if flight.lowestPrice < dest["lowestPrice"]:
        to_send = f"Low Price Alert! Only {flight.lowestPrice} PLN to fly from " \
                  f"{flight.departure_city} | {flight.departure_airport_code} " \
                  f"to {flight.dest_city} | {flight.dest_airport_code}, " \
                  f"from {flight.outbound_date} to {flight.inbound_date}.\n"
        link = f"\nhttps://www.google.com/travel/flights?q=Flights%20to%20" \
               f"{flight.dest_airport_code}%20from%20{flight.departure_airport_code}" \
               f"%20on%20{flight.outbound_date}%20through%20{flight.inbound_date}"

        if flight.stop_overs == 0:
            notification.send_sms(
                message=to_send
            )
            notification.send_emails(
                body=to_send+link,
                emails=emails
            )
        else:
            stop_over = f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city} City.\n"
            notification.send_sms(
                message=to_send+stop_over
            )
            notification.send_emails(
                body=to_send+stop_over+link,
                emails=emails
            )
