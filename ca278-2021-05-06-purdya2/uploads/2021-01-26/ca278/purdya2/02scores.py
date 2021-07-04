#!/usr/bin/env python

dict = {  # creating dictionary
   "Draws" : 0,
   "Wins" : 0,
   "Losses" : 0,
}

scores = raw_input("Please enter a list of scores:").split()

for score in scores:
   if score == "1":
      dict["Draws"] = dict["Draws"] + 1
   elif score == "3":
      dict["Wins"] = dict["Wins"] + 1
   else:
      dict["Losses"] = dict["Losses"] + 1

print "Draws:", dict["Draws"]
print "Losses:", dict["Losses"]
print "Wins:", dict["Wins"]
