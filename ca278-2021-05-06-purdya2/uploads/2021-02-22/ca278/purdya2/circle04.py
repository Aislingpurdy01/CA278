#!/usr/bin/env python

from math import pi

class Circle:
   ''' This is a circle class '''
   def __init__(self, radius):
      self.radius = radius

   def get_area(self):
      ''' return area of the circle. '''
      return pi * self.radius ** 2

   def get_circumference(self):
      ''' return the circumference of the circle. '''
      return 2 * pi * self.radius
