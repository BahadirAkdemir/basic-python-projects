import requests, datetime

APPLICATION_ID = ""
APPLICATION_KEY = "" 
header = {

    "x-app-id":APPLICATION_ID,
    "x-app-key":APPLICATION_KEY,

}

parameters = {
    "query": "Ran 2 miles and walked for 3Km."

}
nutritionix_url="https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=nutritionix_url,json=parameters, headers=header)
data=response.json()

sheety_bearer_headers = {
"Authorization": "YOUR_TOKEN"
}
sheety_url=""

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_url, json=sheet_inputs, headers=sheety_bearer_headers)
    print(sheet_response.text)


