#!/usr/bin/env python


class BankAccount:
   ''' This is a class definition for a bank account '''
   id_counter = 0

   def __init__(self, balance):
	   self.balance = balance
      BankAccount.id_counter = BankAccount.id_counter + 1
      self.id = BankAccount.id_counter

   def __str__(self):
      ''' This retruns the account information '''
      return "Account Number: " + str(self.id) + "Balance: \n" + str(self.balance)

   def lodge(self, amount):
      ''' This lodges the amount of money into the account '''
      self.balance = self.balance + amount  # doesnt need return statment. not returning info

   def withdraw(self, amount):
      ''' This withdraws money from the account '''
      self.balance = self.balance - amount  # takes the withdraw amount away from bank balance



if __name__ == "__main__":
   acc1 = BankAccount(1000)
   print acc1
   acc2 = BankAccount(1500)
   print acc2
   acc1.lodge(500)
   print acc1
   acc2.withdraw(500)
   print acc2
