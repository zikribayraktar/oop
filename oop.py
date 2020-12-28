#!/usr/bin/env python3
"""
Sample OOP in Python
https://www.python-boilerplate.com/
To run this code, go to your shell, and type in:
>> python ./oop.py
"""

__author__ = "Zikri Bayraktar, Ph.D."
__version__ = "0.1.0"
__license__ = "MIT"

###############################################################
###############################################################

"""Custom Exception"""
class BalanceError(Exception): pass

class CUSTOMER(object):
    """
    Simple Object definition
    """
    MIN_AGE = 18 ## Class attribute, shared among all instances.

    """ Instance initialization method
        Inputs are expected at instance creation"""
    def __init__(self,name,age,id,balance):
        self.name = name
        self.id = id
        print('Init called')
        if age >= CUSTOMER.MIN_AGE:
            self.age = age
        else:
            self.age = CUSTOMER.MIN_AGE
        
        ## Handle negative balance error:
        if balance < 0:
            raise BalanceError('Balance has to be non-negative!')
        else:
            self.balance = balance
    
    ## will be called when == is used between two instances
    ## (other comparisons can be made too, __lt__, __gt__, __ne__)
    def __eq__(self,other):
        ## return a bolean True/False
        return (self.id == other.id) and (self.name == other.name) and (self.age == other.age)

    """ Class Method for Alternative Initialization
        To read data from file"""
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.readline()
            age = f.readline()
            id = f.readline()
            balance = f.readline()
            return cls(name.rstrip(), int(age), int(id), int(balance))

    """ Other methods at instance creation"""
    def identify(self):
        print('My name is {} and I am {} years old.'.format(self.name,self.age))

###############################################################
###############################################################

""" Create a new class named bank account"""
class BankAccount(object):
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        self.balance -= amount

""" Inherit from bank account class
    SavingsAccount is-a BankAccount"""
class SavingsAccount(BankAccount):
    ## Constructor specifically for SavingsAccount with an additional parameter
    def __init__(self,balance,rate):
        ## Call the parent constructor first:
        BankAccount.__init__(self,balance)
        ## Add more functionality:
        self.interest_rate = rate
    
    ## Add interest rate functionality:
    def compute_interest(self, n_periods=1):
        return self.balance*((1+self.interest_rate)**n_periods-1)

""" Inherit from bank account class
    CheckingAccount is-a BankAccount """
class CheckingAccount(BankAccount):
    def __init__(self,balance,limit):
        BankAccount.__init__(self,balance)
        self.limit = limit
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount, fee=0):
        if fee <= self.limit:
            BankAccount.withdraw(self, amount-fee)
        else:
            BankAccount.withdraw(self, amount - self.limit)


###############################################################
###############################################################

"""Example of how to use @property for protected attributes"""
class Employee(object):
    def __init__(self, name, new_salary):
        """Use @property for protected attribute"""
        self._salary = new_salary  ## note the _ before attribute

    ## use @property decorator
    ## and use the name of the attribute to define method:
    @property
    def salary(self):
        return self._salary
    
    ## use the attributename.setter decorator:
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid salary")
        self._salary = new_salary
## Additional Notes:
## If you do not add @attributename.setter,
## then you will create a read-only property
## If you add @attributename.getter,
## then you can use for the method that is called when the property's value is retrieved
## if you add @attributename.deleter,
## then you can use for the method that is called when the property is deleted using del.


###############################################################
###############################################################

def main():
    ## Create a new instance, i.e. a new customer:
    zikri = CUSTOMER('Zikri', 21, 777, 0)
    zikri.identify()

    ## Create a new instance by reading the data from file:
    newOne = CUSTOMER.from_file('new_customer.txt')
    newOne.identify()

    ## Test if two objects are equal
    print(zikri==newOne)

    ## Testing the protected attributes of a class:
    emp = Employee("Zikri", 100)
    emp.salary = 200
    print(emp.salary)
    emp.salary = -100  ## this will return an error

###############################################################
###############################################################

if __name__ == "__main__":
    main()