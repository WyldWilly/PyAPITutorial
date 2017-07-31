#!/usr/bin/env python3

import requests

parameters = {"lat": 40.44, "lon": -79.99}

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.content.decode("utf-8"))
print(response.status_code)

response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.status_code)

response = requests.get("http://api.open-notify.org/iss-pass.json?", params=parameters)
print(response.content.decode("utf-8"))
