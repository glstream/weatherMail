import smtplib
from darksky import forecast
import inspect
import darksky


key = "43c6b72e8be91162c3aa43f4f87be22d"
lat = "47.57070050000001"
lon = "-122.38715259999998"
myHouse = forecast(key, lat, lon)


user = "starbuckswork01@gmail.com"
password = "xxxxxxxxxxxxxx"
recipient = "grayson.stream@gmail.com"
body = """
Hello Sailor from python code! {0}
""".format(
    myHouse.temperature
)


print(myHouse.temperature)
print(myHouse.daily.summary)
print(myHouse.apparentTemperature)
print(myHouse.summary)


try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.login(user, password)
    print("Server Logged In")

    server.sendmail(user, recipient, body)
    server.close()
    print("Email has been sent")
except:
    print("Something went wrong...")

