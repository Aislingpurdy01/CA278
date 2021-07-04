#!/usr/bin/env python

with open("file.txt", "r") as f:
   for line in f:
      line = line.strip()
      print line

