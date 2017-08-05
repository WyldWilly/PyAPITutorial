#!/usr/bin/env python3

import requests, json

# response = requests.get(...)
# json_data = json.loads(response.text)

payload = requests.get("http://api.open-notify.org/astros.json")
payload_json = json.loads(payload.text)

print(payload_json)

for name in payload_json:
    print(name)

for message in payload_json:
    print(message)
