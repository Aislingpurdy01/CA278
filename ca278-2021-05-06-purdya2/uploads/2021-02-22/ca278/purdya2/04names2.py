#!/usr/bin/env python

import sys

file = sys.argv[1]

with open(file, "r") as f:
   lines = f.readlines()
   for line in lines:
      print line.split()[0]
