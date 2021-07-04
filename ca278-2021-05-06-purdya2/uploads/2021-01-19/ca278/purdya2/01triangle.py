#!/usr/bin/env python

a = input()
b = input()
c = input()

if a == b == c:
   print "equilateral"
elif a == b != c:
   print "isosceles"
elif a == c != b:
   print "isosceles"
elif b == c != a:
   print "isosceles"
else:
   print "neither"
