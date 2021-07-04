#!/usr/bin/env python

n = input("Please enter a number (-1 to stop):")
a = []

while n != -1:
   if n not in a:  # removing duplicates
      a.append(n)
   n = input("Please enter a number (-1 to stop):")
print a
