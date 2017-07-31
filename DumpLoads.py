#!/usr/bin/env python3

import json

# Make a list of fast food chains.
best_food_chains = ["taco Bell", "Shake Shack", "Chipolte"]

# This is a list.
print(type(best_food_chains))

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)

# We've successfully converted our list to a string
print(type(best_food_chains_string))

# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))
