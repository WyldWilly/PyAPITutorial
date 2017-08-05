#!/usr/bin/env python3

#http://python-guide-pt-br.readthedocs.io/en/latest/scenarios/serialization/

import pickle

# Here's an example dict
grades = {'Alice': 89, 'Bob': 72, 'Charles': 87}

# Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps(grades)
print(grades)

# Use loads to de-serialize an object
received_grades = pickle.loads(serial_grades)
print(received_grades)

for name in grades:
    print(name)
