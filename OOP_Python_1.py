#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:32:43 2020

@author: rakhengarg
"""

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
        self.salary = int(self.salary * Employee.raise_amount)
        return self.salary

emp_1 = Employee('Rakhen', 'Garg', 'Intel', 10000)
emp_2 = Employee('Robin', 'Malik', 'Ndsu', 20000)

# Two different ways to call the class
#print(Employee.fullname(emp_1))
#print(emp_1.fullname())

#Demo for accessing class variable both from class and instances
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#Checking who contains the class variable
#print(Employee.__dict__)  #Retuns the class variable
#print(emp_1.__dict__)     #Does not contains class variable

#Changing raise amount for a specific employee and seeing its impact on others
#emp_1.raise_amount = 1.05
#print(Employee.raise_amount)
#print(emp_1.raise_amount)     #Amount changes only for this
#print(emp_2.raise_amount)

#Testing salary raise gets applied
#print(Employee.apply_raise(emp_2))







        
