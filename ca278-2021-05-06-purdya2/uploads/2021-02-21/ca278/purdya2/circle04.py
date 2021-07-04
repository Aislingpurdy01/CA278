#!/usr/bin/env python

from math import pi

class Circle:
   ''' This is a circle class '''
   def _init_(self, radius):
      self.radius = radius

   def get_area(self):
      ''' return area of the circle. '''
      return pi * self.radius ** 2

   def get_circumference(self):
      ''' return the circumference of the circle. '''
      return 2 * pi * self.radius

if __name__ == '__main__':
   print "Area:" + " " + Circle(radius).get_area()
   print "Circumference:" + " " + Circle(radius).get_area()
