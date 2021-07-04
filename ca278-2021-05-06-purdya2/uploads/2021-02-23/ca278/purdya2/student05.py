#!/usr/bin/env python

class Student:
   ''' This is a class definition for a student '''
   def __init__(self, name, exam, ca):
      self.name = name
      self.exam = exam
      self.ca = ca

   def get_average(self):
      ''' Return the average mark of ca + exam '''
      return (self.exam + self.ca) / len(self.exam + self.ca)

   def __str__(self):
      return 'Name: ' + str(self.name) + 'Average: ' + str(self.get_average)

# if __name__ = '__main__':
#    student = Student(name, exam, ca)


