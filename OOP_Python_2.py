#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:41:36 2020

@author: rakhengarg
"""

#Learning about difference between regular methods, class methods and static methods
#Regular methods automatically pass the instance as the first arguments i.e.: self. 
#Class methods automatically pass class as the first argument i.e.: cls.
#Static methods do not pass anything automatically neither the instance nor class.

class Employee:
    
    #Initializing class variable: A variable that is shared across all the instances of the class
    raise_amount = 1.04
    
    
    #Method_1
    def __init__(self, first, last, company, salary):
        #Defining instance variables
        self.first = first
        self.last = last
        self.salary = salary
        self.company = company
        self.email = first + '.' + last + '@' + company + '.com'
        
    #Method_2
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #Method_3
    #Important: Class variables are accessed using class name
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return self.salary
    
    #Method_4
    #Important: Defining Class method. Objective is to remove manual intervention.
    @classmethod
    def set_raise_amt(cls,amount):  #Here cls is convention for class variable i.e.: raise_amount defined above
        cls.raise_amount = amount
        return cls.raise_amount
    
    #Method_5
    #Important: Defining Class method. Objective is to separate the input data to avoid parsing. This too removes manual intervention.
    #example of data: emp_str_1 = 'Jane-Doe-90000'
    @classmethod
    def from_string(cls, emp_str):
        first, last, company, salary = emp_str.split('-')
        return cls(first, last, company, salary)
    
    #Method_6
    #Important: Defining Static method. Checking any passed date is a workday.
    #In python dates have the weekday methods. Monday equals to 0, Sunday equals to 6.
    @staticmethod   #This is called as decorater
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
emp_1 = Employee('Rakhen', 'Garg', 'Intel', 10000)
emp_2 = Employee('Robin', 'Malik', 'Ndsu', 20000)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount) #The output will be 1.04 in these three print statements

#Making use of class method we can change this amount
#Employee.set_raise_amt(1.09)    #emp_1.set_raise_amt(1.09) #Instance can also be used to set raise_amount
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)  #The amount gets changes  for all

#String data, passing the string and printing the output
#emp_str_1 = 'John-Doe-Microsoft-70000'
#emp_3 = Employee.from_string(emp_str_1)
#print(emp_3.email)

#Dealing with the static method
import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

