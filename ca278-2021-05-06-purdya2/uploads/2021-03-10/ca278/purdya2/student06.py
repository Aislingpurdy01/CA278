#!/usr/bin/env python


class Student:
   ''' This is a student class '''

   id_counter = 0

   def __init__(self, name, exam, ca):
      self.name = name
      self.exam = exam
      self.ca = ca
      Student.id_counter = Student.id_counter + 1
      self.id = Student.id_counter

   def get_average(self):
      ''' This returns the average mark '''
      return (self.exam + self.ca) / 2

   def __str__(self):
      ''' This returns the students name followed by their average mark '''
      return "Id: " + str(self.id) + ", Name: " + self.name +", Average: " + str(self.get_average())




if __name__ == "__main__":
   with open("students.txt", "r") as f:
      for line in f:
         information = line.split(",")
         student = Student(information[0], float(information[1]), float(information[2]))
         print student
