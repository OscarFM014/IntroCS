'''
Created on 15/01/2018

@author: Oscar
'''
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.
# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big=biggest(a,b,c)
    if big ==a:
        return bigger(c,b)
    if big ==c:
        return bigger (a,b)
    else:
         return bigger(a,c)

               
        

print median(9,4,8)

