import time

import requests
import datetime
import smtplib
my_lat = 12.728030
my_lan = 77.827057
my_id = "avatar0041@gmail.com"
my_pass = "avatar123!@#"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if my_lat-5 <=iss_latitude <=my_lat+5 and my_lan-5 <=iss_longitude <=my_lat+5:
        return True

def is_dark():
    parameter = {
        "lat": my_lat,
        "lng":my_lan,
        "formatted":0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour
    if time_now >=sunset or time_now <=sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_id,password=my_pass)
        connection.sendmail(from_addr=my_id,
                            to_addrs=my_id,
                            msg=f"Subject:look up \n\niss is above in the sky")
