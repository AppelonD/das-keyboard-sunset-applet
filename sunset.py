import urllib.request
import datetime
import json

url = 'https://api.sunrise-sunset.org/json?lat=36.7201600&lng=4.4203400&formatted=0&date=today'

req = urllib.request.Request(url)

r = urllib.request.urlopen(req).read()

data = json.loads(r)

k = data["results"]

sunset = k["sunset"]

sunset_time_object = datetime.datetime.fromisoformat(sunset)

print('Solen går ned idag kl:', sunset_time_object.time())

timeis = datetime.datetime.now().strftime("%H:%M:%S")
timeisobject = datetime.datetime.strptime(timeis, "%H:%M:%S")

print('Klokken er nu: ', timeisobject.time())

timeisobject = timeisobject.replace(tzinfo=None)
sunset_time_object = sunset_time_object.replace(tzinfo=None)

countdown = sunset_time_object - timeisobject

seconds = countdown.seconds

# 1 day = 86400 Sec's

while seconds > 86400:
    print('Sekunder tilbage før solnedgang :', countdown.seconds)
