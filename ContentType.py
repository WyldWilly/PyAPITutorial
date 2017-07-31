#!/usr/bin/env python3

import requests

# Make the same request we did earlier, but with the coordinates of San Francisco instead

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Headers is a dictionary
print(response.headers)


# Get the content-type from the dictionary.
print(response.headers["content-type"])
