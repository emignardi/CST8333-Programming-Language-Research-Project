import requests

api_url = "https://api-web.nhle.com/v1/club-schedule-season/TOR/now"

jsonResponse = requests.get(api_url).json()

print(jsonResponse)