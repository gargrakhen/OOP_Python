#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:40:11 2020

@author: rakhengarg
"""

#Understanding sub-class concept

#Class_1
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
    
#Class_2
class Developer(Employee):
    raise_amount = 1.8
    def __init__(self, first, last, company, salary, prog_lan):
        #Instead of defining same class instances (first, last, company, salary) again and again we will use super as it will fetch the data from employee class
        super().__init__(first, last, company, salary)
        self.prog_lan = prog_lan
        
#Class_3
class Manager(Employee):
    #We will be initializing instance for employees
    def __init__(self, first, last, company, salary, employees=None):
        super().__init__(first, last, company, salary)
        if employees is None: 
            self.employees = []
        else:
            self.employees = employees
            
    #Method for adding employees in the list
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    #Method for removing employees from the list
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    #Method for printing names of employee that manager had supervised
    def print_emps(self):
        for emp in self.employees:
            print('---->', emp.fullname())
    
#Now if we use Employee class then it won't use the raise value that we had initialized in the developer class.
#dev_1 = Employee('Rakhen', 'Garg', 'Intel', 10000)
#dev_2 = Employee('Robin', 'Malik', 'Ndsu', 20000)

#print(dev_1.salary)
#dev_1.apply_raise()
#print(dev_1.salary)

#If we don't have init statement in developer class and we write just pass and run the below command we will come to know about the hierarchy
#print(help(Developer))
        
dev_1 = Developer('Rakhen', 'Garg', 'Intel', 10000, 'Python')
dev_2 = Developer('Robin', 'Malik', 'Ndsu', 20000, 'Java')

mgr_1 = Manager('Aaron', 'Coleman', 'Intel', 30000, [dev_1])
#print(mgr_1.fullname())

#mgr_1.add_emp(dev_1)
#mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.print_emps()


#Understanding python built-in functions
#To check object is instance of which class. The below statement will return true or false
print(isinstance(mgr_1, Manager))



