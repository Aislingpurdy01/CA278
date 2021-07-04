#!/usr/bin/env python

n = input("Enter a number:")

sum = 0
print "\n" + str(n)

while n > 0:
   sum = sum + n
   n = n - 1
   print n

print "\n" + str(sum)
