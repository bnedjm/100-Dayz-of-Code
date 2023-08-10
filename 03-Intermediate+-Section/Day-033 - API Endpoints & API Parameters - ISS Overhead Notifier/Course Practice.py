import requests
from datetime import *

MY_LAT = 52.525578
MY_LNG = 13.373325

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

current_time = datetime.now()

print(sunrise)
print(sunset)


print(current_time.hour)
