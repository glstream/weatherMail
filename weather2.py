import forecastio


lat = "47.57070050000001"
lng = "-122.38715259999998"


forecast = forecastio.load_forecast(api_key, lat, lng)

byHour = forecast.hourly()
print(byHour.summary)
print(byHour.icon)

for hourlyData in byHour.data:
    print(hourlyData.temperature)

