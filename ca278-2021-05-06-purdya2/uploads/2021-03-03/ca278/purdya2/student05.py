#!/usr/bin/env python

# corrected version:
class Student:
   ''' This is a class definition for a student '''
   def __init__(self, name, exam, ca):
      self.name = name
      self.exam = exam
      self.ca = ca

   def __str__(self):
      return 'Name: ' + self.name +', Average: ' + str(self.get_average())

   def get_average(self):
      ''' Return the average mark of ca + exam '''
      return (self.exam + self.ca) / 2


if __name__ == '__main__':
   with open('students.txt', 'r') as f:  # file with studnet names
      for line in f:
         information = line.split(",")  # student information
         student = Student(information[0], float(information[1]), float(information[2]))
         print student
