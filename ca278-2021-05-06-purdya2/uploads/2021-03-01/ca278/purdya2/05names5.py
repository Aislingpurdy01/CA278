#!/usr/bin/env python

class Person:
   ''' This is a class definition for a person '''
   def __init__(self, n, a):
      self.n = n  # name
      self.a = a  # age

   def get_surname(self):
      ''' Returns the surname '''
      return self.n.split()[1]

   def get_firstname(self):
      ''' Returns the firstname '''
      return self.n.split()[0]

   def __str__(self):
      ''' Return the surname, firstname and age '''
      surname = self.get_surname()
      firstname = self.get_firstname()
      return surname + ", " + firstname + " (" + self.a + ")"

if __name__ == '__main__':
   name = raw_input('What is your name?')
   age = raw_input('How old are you?')
   person = Person(name, age)
   print 'Hello', person.get_firstname()
   print 'Here are your details:\n', person.__str__()
