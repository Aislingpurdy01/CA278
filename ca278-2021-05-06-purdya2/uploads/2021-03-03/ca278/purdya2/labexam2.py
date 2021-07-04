#!/usr/bin/env python

dict = {
   "Austria" : 16,
   "Ecudor" : 16,
   "North Korea" : 17,
   "Sudan" : 17,
   "Ireland" : 18,
   "Portugal" : 18,
   "Russia" : 18,
   "Cameroon" : 20,
   "Bahrain" : 20,
   "Lebanon" : 21,
}

age = input("How old are you?")
country = raw_input("Where are you from?").lower()  # make case insensitive

# for countries in dict:
#    if age >= 16:
#       print "You can vote"
#    else:
#       print "I do not know whether you can vote" 
i = 1
countries = country[0]
while i < len(country):
   countries = countries + country[i]
   i = i + 1

if country in dict:
   if age >= int(dict[countries]):
      print "You can vote"
   elif age < int(dict[countries]):
      print "You cannot vote"
else:
   print "I do not know whether you can vote"
  