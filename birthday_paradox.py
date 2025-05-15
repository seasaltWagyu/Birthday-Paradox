from random import *
from math import *

"""
purpose is to simulate the birthday paradox probabilities, highlighting how
the probability of a duplicate birthday in a group of people (in this case, a class of 38 students) is
higher than what your intuition may think
"""

__author__ = "seasaltWagyu"

class Student:
    def __init__(self):
        self.birthday = randint(1, 365) #simulating the random birthday of every student

class Class:
    def __init__(self):
        self.people = [Student() for i in range(37)] #creating a class of 38 students with random birthdays
        
def birthday_same():
    
    """
    a helper function to check if the class of 38 students
    has 2 people that share the same birthday
    """
    
    my_class = Class()
    
    birthday_list = [student.birthday for student in my_class.people] #the list of birthdays of every student in my_clsas
    
    for birthday in birthday_list:
        if birthday_list.count(birthday) > 1: #if two students share a same birthday...
            return True  #return True
        
        else:
            if birthday_list[-1] == birthday: #if it is the last birthday in a list, indicating no duplicate birthdays...
                return False   #return False
            else:
                continue

def probability_same():
    
    """
    function that creates 100,000 classes and sees 
    how many of them have students with the same birthday
    """
    
    same_birth = [birthday_same() for i in range(10 * 10**4)]  #simulating these classes of 38 students 100,000 times
    
    return floor((same_birth.count(True)/len(same_birth))*100)    #dividing the amount of Trues by the list-size to get the probability any two students in a class of 38 share a birthday

def main():
    
    """
    main function -> calls the probability functions
    """
    
    print(f"The probability of any two students in a class of 38 students having the same birthday is {probability_same()}% over a random data set of 100,000 simulated classes.")


main()
