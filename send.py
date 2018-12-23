import smtplib
from darksky import forecast
import inspect
import darksky
from configs import *

key = "43c6b72e8be91162c3aa43f4f87be22d"
lat = "47.57070050000001"
lon = "-122.38715259999998"
myHouse = forecast(key, lat, lon)


user = "starbuckswork01@gmail.com"
recipient = "grayson.stream@gmail.com"

body = """\
Subject: Daily Weather Email
Currently the weather is: {0} degress \n
It Feels like: {1} degress\n
The wind is: {2}mph\n
Summary for the day: {3}
""".format(
    myHouse.temperature,
    myHouse.apparentTemperature,
    myHouse.windSpeed,
    myHouse.daily.data[0].summary,
)

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.login(user, pwd)
    print("Server Logged In")

    server.sendmail(user, recipient, body)
    server.close()
    print("Email has been sent")
except:
    print("Something went wrong...")

