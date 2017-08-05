#!/usr/bin/env python3

#https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183

import requests, json, datetime
import pickle

# ---------------------------------------------------------
# Simple Object Graph
# The simple object graph is a dictionary that contains a
# listof integers, a string, a float, a boolean, and a None.
# ---------------------------------------------------------

simple = dict(int_list=[1, 2, 3],
              text='string',
              number=3.44,
              boolean=True,
              none=None)

# ---------------------------------------------------------
# Complex Object Graph
# The complex object graph is also a dictionary, but
# it contains a datetime object and user-defined class
# instance that has a self.simple attribute, which
# is set to the simple object graph.
# ---------------------------------------------------------

class A(object):
    def __init__(self, simple):
        self.simple = simple

    def __eq__(self, other):
        if not hasattr(other, 'simple'):
            return False
        return self.simple == other.simple

    def __ne__(self, other):
        if not hasattr(other, 'simple'):
            return True
        return self.simple != other.simple


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return {'__datetime__': o.replace(microsecond=0).isoformat()}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


complex = dict(a=A(simple), when=datetime.datetime(2016, 3, 7))

# ---------------------------------------------------------
# Pickle
# Pickle is a staple. It is a native Python object serialization
# format. The pickle interface provides four methods: dump, dumps,
# load, and loads. The dump() method serializes to an open file
# (file-like object). The dumps() method serializes to a string.
# The load() method deserializes from an open file-like object.
# The loads() method deserializes from a string.
# ---------------------------------------------------------

pickle.dumps(simple)

"(dp1\nS'text'\np2\nS'string'\np3\nsS'none'\np4\nNsS'boolean'\np5\nI01\nsS'number'\np6\nF3.4399999999999999\nsS'int_list'\np7\n(lp8\nI1\naI2\naI3\nas."

pickle.dumps(simple, protocol=pickle.HIGHEST_PROTOCOL)
'\x80\x02}q\x01(U\x04textq\x02U\x06stringq\x03U\x04noneq\x04NU\x07boolean\x88U\x06numberq\x05G@\x0b\x85\x1e\xb8Q\xeb\x85U\x08int_list]q\x06(K\x01K\x02K\x03eu.'


# ---------------------------------------------------------
# JSON
# JSON (JavaScript Object Notation) has been part of the Python
# standard library since Python 2.5. I'll consider it a native
# format at this point. It is a text-based format and is the unofficial
# king of the web as far as object serialization goes. Its type system
# naturally models JavaScript, so it is pretty limited.
#
# Let's serialize and deserialize the simple and complex objects
# graphs and see what happens. The interface is almost identical to
# the pickle interface. You have dump(), dumps(), load(), and loads()
# functions. But, there are no protocols to select, and there are many
# optional arguments to control the process. Let's start simple by
# dumping the simple object graph without any special arguments:
# ---------------------------------------------------------
null = None
simple = {"text": "string", "none": null, "boolean": True, "number": 3.44, "int_list": [1, 2, 3]}

print(json.dumps(simple, indent=4))

serialized = json.dumps(complex, indent=4, cls=CustomEncoder)

print(serialized)


