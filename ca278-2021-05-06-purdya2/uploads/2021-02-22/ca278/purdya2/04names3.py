#!/usr/bin/env python
import sys

file = sys.argv[1]

names = []
surname = raw_input("Please enter a surname:")

with open(file, "r") as f:
   lines = f.readlines()
   for line in lines:
      firstname = line.split()[0]  # firstname is first position
      secondname = line.split()[1]  # surname is second posistion
      if surname.lower() == secondname.lower():
         names.append(firstname)

   if len(names) == 0:
      print "No-one has that surname"
   else:
      print names
