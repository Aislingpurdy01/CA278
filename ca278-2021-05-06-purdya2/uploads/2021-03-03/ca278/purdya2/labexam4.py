#!/usr/bin/env python

import sys

file = sys.argv[1]
dict = {}


with open(file, "r") as f:
   lines = f.readlines()
    key, value = line.split()  # convert file to dictionary
      dict[key] = value
   user_data = raw_input("Enter name,age,country:").lower().split(",")
   for line in lines:
      if user_data[2] in lines:
         print "You can vote"
