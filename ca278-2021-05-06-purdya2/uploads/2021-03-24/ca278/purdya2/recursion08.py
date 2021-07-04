#!/usr/bin/env python

# import time

# def countdown(num):
#    ''' Prints the numbers num to 1 with 100 milliseconds gap '''
#    if num > 0:
#    	  time.sleep(0.1)
#    	  print num
#       print "LIFT OFF"
#    else:
#       print countdown(num - 1)
#       print "LIFT OFF"


def search(the_str, letter):
	''' Returns True if the letter is in the_str, else returns False '''
	if the_str == []:
	   return False
	elif the_str[0] == letter:
	   return True
	else:
	   return search(the_str[1:], letter)


def previous_two(n):
   ''' Returns the value of the sequence at a particular position '''

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