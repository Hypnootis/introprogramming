import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

strongest_wind = [0, 0]
weakest_wind = [999, 999]

for i in weather:
    if i["wind"] > strongest_wind[0]:
        strongest_wind.clear()
        strongest_wind.insert(0, i["wind"])
        strongest_wind.insert(1, i["location"])
    else:
        if i["wind"] < weakest_wind[0]:
            weakest_wind.clear()
            weakest_wind.insert(0, i["wind"])
            weakest_wind.insert(1, i["location"])



print(f"Strongest wind today at location: {strongest_wind[1]}, {strongest_wind[0]} m/s")
print(f"Weakest wind today at location: {weakest_wind[1]}, {weakest_wind[0]} m/s")
