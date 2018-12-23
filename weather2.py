import forecastio
from configs import *

lat = "47.57070050000001"
lng = "-122.38715259999998"


forecast = forecastio.load_forecast(api_key, lat, lng)

current = forecast.currently()
print(current.summary)
print(current.icon)

# for hourlyData in byHour.data:
#     print(hourlyData.temperature)

