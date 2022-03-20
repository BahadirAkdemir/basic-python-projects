api_key = ""
appid="appid"
my_city = "q=Kayseri,TR"
get_weather = "weather?"
get_one_call = "onecall?"
lat="lat"
lon="lon"
exclude="exclude"
my_excludes = "minutely,hourly,daily,alerts,flags".split(",")
url = "http://api.openweathermap.org/data/2.5/"

import requests
import json



#data_weather = requests.get("http://api.openweathermap.org/data/2.5/"+get_weather+my_city+"&"+"appid="+api_key)
#print(data_weather.text)
onecall_params = {
    lat: "38.73",
    lon: "35,49",
    exclude: my_excludes[0]+","+my_excludes[2]+","+my_excludes[3]+","+my_excludes[4],
    appid: api_key
}
data_one_call = requests.get("https://api.openweathermap.org/data/2.5/"+get_one_call,onecall_params)
data_weather = data_one_call.json()


umbrella=False
for i in data_weather["hourly"][7:20]:
    if (i["weather"][0]["id"]) < 700:
        umbrella = True
        break

if umbrella:
    print("Umbrella is needed")
else:
    print("Umbrella is not needed")

#print(data_one_call.text)


