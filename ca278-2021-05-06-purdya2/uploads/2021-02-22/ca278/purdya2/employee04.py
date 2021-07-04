#!/usr/bin/env python

class Employee:
   ''' This is an Employee class definition. '''

   def __init__(self, name, job_desc, salary):
      self.name = name
      self.job_desc = job_desc
      self.salary = salary

   
   def net_salary(self):
      '''Return net salary.'''
      return self.salary * 0.80

if __name__ == '__main__':
   name = raw_input("Enter the employee name:\n")
   job_desc = raw_input("Enter the employee job description:\n")
   salary = input("Enter the employee salary:\n")
   employee = Employee(name, job_desc, salary)
   print "Net Salary:", employee.net_salary()  #note: cant concatnate string and float. Must use ","
