#!/usr/bin/env python

from math import pi

class Circle:
   ''' This is a class definition for a circle '''
   def __init__(self, radius):
      self.radius = radius

   def get_area(self):
      ''' returns the area of the circle '''
      return pi * self.radius ** 2

   def get_circumference(self):
      ''' returns the circumference of the circle '''
      return 2 * pi * self.radius

   def __str__(self):
      ''' returns string and radius '''
      return "circle with radius " + str(self.radius)

   def __eq__(self, other):
      ''' returns true if same radius value. else, returns false '''
      if self.radius == other.radius:
         return True
      else:
         return False


if __name__ == "__main__":
   radius_1 = Circle(input("Enter the radius of the first circle:" + "\n"))
   radius_2 = Circle(input("Enter the radius of the second circle:" + "\n"))
   print radius_1
   print radius_2
   print "Are they equal?"
   if radius_1 == radius_2:
      print "yes"
   else:
      print "no"
