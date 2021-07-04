#!/usr/bin/env python

#  price functions:
def get_price(age):
   if age <= 16:
      price = 5
   elif age > 60:
      price = 7
   else:
      price = 10
   return price

#  upper and lower case string output
def weird_case(some_str):
   strings = some_str.split()
   output = ""
   position = 0
   for string in strings:
      for letter in string:
         if position % 2 != 0:
            output = output + letter.lower()
         else:
            output = output + letter.upper()
         position = position + 1
      output = output + " "
   return output.strip()  # strip whitespace

#  every second element
def every_second(l1,l2):
   l3 = []
   i = 0
   while i < len(l1):
      if i % 2 == 1:
         l3.append(l1[i])
      i = i + 1

   i = 0
   while i < len(l2):
      if i % 2 == 1:
         l3.append(l2[i])
      i = i + 1
   return l3

#  true for negative numbers
def is_neg(num):
   if num < 0:
      return True
   else:
      return False

#  remove negative number from list
def remove_neg(lst):
   n = []  # list negative
   for num in lst:
      if num < 0:
         n.append(num)
   for num in n:
      lst.remove(num)  # remove negative number

#  print all numbers from num to 1(gap of 100 milliseconds)
import time

def countdown(num):
   while num > 0:
      print num
      num = num - 1
      time.sleep(0.1)  # insert pause of 100 millisecond
   print "LIFT OFF!"

#  retrun true if letter is in str, else: false
def search(str,letter):
   if letter in str:
      return True
   else:
      return False

#  return posistion of first occurence, else -1
def index(str,letter):
   position = 0
   if letter in str:
      position = position + 1
      return position
   else:
      return -1

#  value in particular postion
def previous_two(n):
   seq = []
   i = 1
   while i < n:
      seq.append(seq[i] + seq[i - 1])
      i = i + 1
   return seq[n]
