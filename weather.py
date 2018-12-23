from darksky import forecast
import inspect
import darksky


key = "43c6b72e8be91162c3aa43f4f87be22d"
lat = "47.57070050000001"
lon = "-122.38715259999998"


myHouse = forecast(key, lat, lon)

print(myHouse.temperature)
print(myHouse.daily.summary)
print(myHouse.apparentTemperature)
print(myHouse.summary)

