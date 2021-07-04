#!/usr/bin/env python

class Voter:
   ''' This is a class definition for a voter '''
   def __init__(self, name, age, nationality):
      self.name = name
      self.age = age
      self.nationality = nationality

i = 1
country = []
countries = country[0]
while i < len(country):
   countries = countries + country[i]
   i = i + 1

   def can_vote(self):
      ''' Returns True is eligble to vote, else retruns False '''
      if country in dict and age >= int(dict[countries]):
         return True
      else:
         return False

   def __str__(self):
      ''' Returns the voters information '''
      return self.name + " (" + self.age + ")" + " ," + self.nationality

if __name__ == '__main__':
   user_data = raw_input("Enter name, age, country:").lower()
   information = user_data.split(",")  # user's information
   voter = Voter(name, age, nationality)
   print voter.__str__()
   print "You cannot vote\n"