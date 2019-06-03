'''
Created on 26/01/2018

@author: Oscar
'''
# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def set_range(a,b,c):
    big=biggest(a,b,c)
    if big==a:
        ei=bigger(c,b)
        if ei==b:
            return a-c
        else:
            return a-b
    if big ==c:
        si=bigger (a,b)
        if si==a:
            return c-b
        else:
            return c-a
    else:
        bi=bigger(a,c)
        if bi==a:
            return b-c
        else:
            return b-a
    


print set_range(3, 92, 103)
#>>> 6  # since 10 - 4 = 6