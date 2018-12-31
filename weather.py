from darksky import forecast
from configs import *


key = "43c6b72e8be91162c3aa43f4f87be22d"
lat = "47.57070050000001"
lon = "-122.38715259999998"


forecast = forecast(api_key, lat, lon)

icon = forecast.currently.icon
temperature = forecast.currently.temperature
feelsLike = forecast.currently.apparentTemperature
windSpeed = forecast.currently.windSpeed
summary = forecast.hourly.summary

print(icon)
print(temperature)
print(feelsLike)
print(windSpeed)
print(summary)
