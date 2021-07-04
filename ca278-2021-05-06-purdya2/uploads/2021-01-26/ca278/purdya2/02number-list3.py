#!/usr/bin/env python

n = input("Please enter a number (-1 to stop):")
a = []
times = {}

while n != -1:
   if n not in a:
      a.append(n)
      times[n] = 1
   else:
      times[n] = times[n] + 1
   n = input("Please enter a number (-1 to stop):")

print a
for time in times:
   print time, "occurred", times[time], "times"
