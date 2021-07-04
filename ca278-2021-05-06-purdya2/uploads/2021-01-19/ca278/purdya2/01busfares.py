#!/usr/bin/env python

age = input("Please enter your age:")
basic = 0.75

if 5 > age:
   print "You go free!"
elif 5 <= age <= 16:
   print "Your fare is: " + str(basic) + " " + "euro."
elif 17 <= age <= 20:
   print "Your fare is: " + str(basic + 0.50) + " " + "euro."
elif 21 <= age <= 64:
   print "Your fare is: " + str(basic + 0.75) + " " + "euro."
else:
   print "You go free!"
