#!/usr/bin/env python

class Person:
   ''' This is a class definition for a person '''
   def __init__(self, n, a):
      self.n = n  # naem
      self.a = a  # age

   def get_surname(self, n):
      ''' Returns the surname '''
      return self.n[1]

   def get_firstname(self, n):
      ''' Returns the firstname '''
      return self.n[0]

   def __str__(self):
      ''' Return the surname, firstname and age '''
      return 'Surname: ' + str(self.n[1]) + '\nFirst name: ' + str(self.n[0]) + '\nAge: ' + str(self.a)

if __name__ == '__main__':
   person = Person(name, age)
   name = raw_input('What is your name?').split()
   age = input('How old are you?')
   print 'Hello', name[0]
   print 'Here are your details:\n'
   print self.get_surname, self.get_firstname, age
