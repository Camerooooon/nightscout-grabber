# Gets glucose data from nightscout
import os
import time
import requests
from requests.exceptions import HTTPError

key = os.environ.get("NS_API_KEY")
url = os.environ.get("NS_API_URL")

headers = {
    "api-secret": key,
    "accept": "application/json"
}

request_uri = url + "api/v1/times/2/.%2A?count=1"

try:
    response = requests.request("GET", request_uri, headers=headers, timeout=5)
    response.raise_for_status()

    data = response.json()
    arrow_str = data[0]["direction"]
    if arrow_str == "DoubleUp":
        arrow = ""
    elif arrow_str == "SingleUp":
        arrow = ""
    elif arrow_str == "FortyFiveUp":
        arrow = ""
    elif arrow_str == "Flat":
        arrow = ""
    elif arrow_str == "FortyFiveDown":
        arrow = ""
    elif arrow_str == "SingleDown":
        arrow = ""
    elif arrow_str == "DoubleDown":
        arrow = ""
    number = data[0]["sgv"]
    date = data[0]["date"]

    
    local_time = time.time() * 1000
    age = local_time - date
    print(arrow + " " + str(number) + " (" + str(round(age/1000/60)) + "m old)")
except HTTPError as http_err:
    print(f'Failed ):')
except Exception as err:
    print(f'Failed ):')



