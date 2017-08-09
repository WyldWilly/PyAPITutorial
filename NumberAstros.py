#!/usr/bin/env python3

import requests

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 9 people are currently in space
tex = "There are "
after = " astronauts in space currently"
print(data["number"])
print("1 -------")
print(tex, data["number"], after)
print(data)
for name in data:
    print(data[name])

print("2 -------")
response = requests.get("http://api.open-notify.org/astros.json")
print(response.content.decode("utf-8"))

#response = requests.get("http://api.open-notify.org/astros.json")
#people = {response}
#for key, val in people.items():
#    print(key, "=>", val)
