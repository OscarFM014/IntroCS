'''
Created on 12/06/2017

@author: Oscar
'''

x=0
z=2
a=1

z=x
a=z
x=a
print x

s= 'google'

print s[1:3]

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.



def bigger(a,b):
    if a>b:
        return a   
    return b




print bigger(4,4)

#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3



def is_friend(a):
    if a[0]=="D" or a[0]== "N":
        return True         
    else:    
        return False
    
    
print is_friend('Diane')