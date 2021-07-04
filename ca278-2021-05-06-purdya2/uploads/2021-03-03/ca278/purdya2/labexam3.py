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

user_data = raw_input("Enter name,age,country:").lower().split(",")
country = []
i = 1
countries = country[0]
while i < len(country):
   countries = countries + country[i]
   i = i + 1

if country in dict:
   print "Hello", user_data[0]
   if user_data[1] >= int(dict[countries]):  #  user_data[1] is age position
      print "You can vote\n"
   elif user_data[1] < int(dict[countries]):
      print "You cannot vote\n"
else:
   print "I do not know whether you can vote\n"
