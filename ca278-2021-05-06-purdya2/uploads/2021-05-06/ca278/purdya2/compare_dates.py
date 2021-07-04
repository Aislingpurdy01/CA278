#!/usr/bin/env python

class My_Date:
   ''' This is a class definition for a calandar date. '''
   def __init__(self, day, month, year):
      ''' This initialises the attributes of the object self. '''
      self.day = day
      self.month = month
      self.year = year

   def __str__(self):
      ''' Returns all the information: day/month/year. '''
      return str(self.day) + "/" + str(self.month) + "/" + str(self.year)

   def __eq__(self, other):
      ''' If the values are the same it returns True. Else, returns False. '''
      if self.day == other.day and self.month == other.month and self.year == other.year:
         return True
      else:
         return False

   def __lt__(self, other):
      ''' If self occurs before other, True is returned. Else, False. '''
      if self.day < other.day and self.month < other.month and self.year < other.year:
         return True
      else:
         return False

if __name__ =='__main__':
   day = input("Enter day:")
   if 1 > day > 31:
      print "Invalid day. Please enter a value between 1 and 31:"
   month = input("Enter month:")
   if 1 > month > 12:
      print "Invalid day. Please enter a value between 1 and 12:" 
   year = input("Enter year:")
   first = My_Date(day, month, year)
   print "The first date is", first
   day_2 = input("Enter day:")
   if 1 > day_2 > 31:
      print "Invalid day. Please enter a value between 1 and 31:"
   month_2 = input("Enter month:")
   if 1 > month_2 > 12:
      print "Invalid day. Please enter a value between 1 and 12:" 
   year_2 = input("Enter year:")
   second = My_Date(day, month, year)
   print "The second date is", second

   if first == second:
      print "The two dates are the same"
   elif first < second:
      print "The first date is before the second date"
   else:
      print "The frist date is after the second date"

 





