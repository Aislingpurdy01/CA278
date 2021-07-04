#!/usr/bin/env python

class Student:
   ''' This is a class definition for a student '''
   def __init__(self, name, exam, ca):
      self.name = name
      self.exam = exam
      self.ca = ca

   def get_average(self, exam, ca):
      ''' Return the average mark of ca + exam '''
      return (self.exam + self.ca) / len(self.exam + self.ca)

   def __str__(self):
      name = self.name
      average = self.get_average()
      return 'Name: ', name + ', ', 'Average: ', average

with open("students.txt", 'r') as f:  # file with studnet names
   names = f.readlines()

if __name__ == '__main__':
   average = [(self.exam + self.ca) / len(self.exam + self.ca)]
   student = Student(name, exam, ca)
   print self.name
   print student.get_average
