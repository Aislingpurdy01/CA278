#!/usr/bin/env python
import sys

file = sys.argv[1]

with open(file, "r") as f:
   lines = f.readlines()
   surname = input("Please enter a surname:")
   for line in lines:
      if  surname in lines:
         print surname
