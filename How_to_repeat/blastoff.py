'''
Created on 18/01/2018

@author: Oscar
'''
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).


        
def countdown(a):
    print a
    while a>1 or a==1:
        if a==1:
            print "Blastoff"
            break
        else:
            if a>1:
                while a>1:
                    a= a-1
                    print a

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!
