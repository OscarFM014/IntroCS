'''
Created on 22/01/2018

@author: Oscar
'''
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(x):
    five=5
    two=2
    one=1
    a=0
    b=0
    c=1
    z=0
    cinco=0
    dos=0
    uno=0
    if x>five or x==5:
        while x>cinco:
            cinco= cinco+five
            if x>cinco or x==5 or x==cinco:
                a=a+1
    cinco=a*five
    if x>(two+cinco) or x==2 or x==two+cinco:
        while x>(dos+cinco):
            dos= dos+two
            if x>(dos+cinco) or x==2 or x==dos+cinco:
                b=b+1
    dos= b*two
    if x>(dos+cinco): 
        return (a,b,c) 
    else:
        return (a,b,z)
    
    


print stamps(6)
