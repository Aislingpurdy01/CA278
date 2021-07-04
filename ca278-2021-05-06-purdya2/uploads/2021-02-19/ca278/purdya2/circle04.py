#!/usr/bin/env python

from math import pi

class Circle:
   ''' This is a circle class '''
   def _init_(self, radius):
      self.radius = radius

   def get_area(self):
      ''' return area of the circle. '''
      return self.radius ** 2 * pi

   def get_circumference(self):
      ''' return the circumference of the circle. '''
      return 2 * pi * self.radius
