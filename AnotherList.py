#!/usr/bin/env python3

import requests

# https://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python
# Creates a list containing 5 lists, each of 8 items, all set to 0
# w, h = 8, 5;
w = 8
h = 5
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][0] = 1
Matrix[1][1] = 5
Matrix[2][1] = 7
Matrix[4][3] = 10
Matrix[4][7] = 11
##Matrix[6][0] = 3 # error! range...
Matrix[0][6] = 3 # valid

print (Matrix[0][0]) # prints 1
x, y = 0, 6
print (Matrix[x][y]) # prints 3; be careful with indexing!
print (Matrix[1][1])
print ("------------------")


for i in Matrix:
    print(i)

print ("------------------")

for j in range(len(Matrix)):
    print (j)

print ("------------------")

for j in Matrix:
    print(j[1])