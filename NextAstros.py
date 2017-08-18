#!/usr/bin/env python3

import requests

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

for people in data['people']:
    print(people['name']+ " " + people['craft'])

