#!/usr/bin/env python

import time

def countdown(num):
   ''' Prints the numbers num to 1 with 100 milliseconds gap '''
   if num == 0:
      print "LIFT OFF!"
   else:
      print num
      num = num - 1
      time.sleep(0.1)
      countdown(num)


def search(the_str, letter):
	''' Returns True if the letter is in the_str, else returns False '''
	if len(the_str) == 0:
	   return False
	elif the_str[0] == letter:
	   return True
	else:
	   return search(the_str[1:], letter)


def previous_two(n):
   ''' Returns the value of the sequence at a particular position '''
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return previous_two(n - 1) + previous_two(n - 2)  # sum of n-1 and n-2
   
if __name__ == "__main__":
   countdown(5)
   if search('python','a'):
      print "W"
   else:
      print "F"
   if search('hello', 'h'):
      print "W"
   else:
      print "F"
#  print previous_two(3)
   print previous_two(6)


##################################################################
# Itterative solutions:

# def countdown(num):
#    while num > 0:
#       print num
#       num = num - 1
#       time.sleep(0.1)  # insert pause of 100 millisecond
#    print "LIFT OFF!"

# def search(str,letter):
#    if letter in str:
#       return True
#    else:
#       return False

# def previous_two(n):
#    seq = []
#    i = 1
#    while i < n:
#       seq.append(seq[i] + seq[i - 1])
#       i = i + 1
#    return seq[n]