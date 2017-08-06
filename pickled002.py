#!/usr/bin/env python3

# source https://www.learnpython.org/en/Serialization

import json, pickle

# There are two basic formats for JSON data. Either in a string
# or the object datastructure. The object datastructure, in Python,
# consists of lists and dictionaries nested inside each other. The
# object datastructure allows one to use python methods (for lists and
# dictionaries) to add, list, search and remove elements from the
# datastructure. The String format is mainly used to pass the data into
# another program or load into a datastructure.
#
# To load JSON back to a data structure, use the "loads" method. This
# method takes a string and turns it back into the json object datastructure:

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])

print(pickle.loads(pickled_string))
print()
#------------------------------------------------------

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it

def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries = json.loads(salaries_json)
    salaries[name] = salary
    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 200, "Jane" : 400, "Me" : 900 }'
new_salaries = add_employee(salaries, "Jon", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
print(decoded_salaries["Jon"])
