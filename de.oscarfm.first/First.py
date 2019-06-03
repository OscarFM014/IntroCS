'''
Created on 05/06/2017
@author: Oscar
'''
from scipy.constants.constants import speed_of_light
print 3
print 1 + 1
print 52 * 3 + 12 * 9
print 52 * (3+12) * 9
print (52*3)+(12*9)
print 362 * 24 * 60 * 60



print 299792458*100*1/1000000000

speed_of_light= 299792458 # meters per second
billionht= 1/1000000000
nanostick= speed_of_light*billionht
print nanostick

cycles_per_second = 2700000000.0 #Billion

print speed_of_light/cycles_per_second 

age= 16
print age*365

print 'hello'

o= "Oscar"#se esta solamente scando una letra
print (o+o)[0]

z="hello bro"#se sigue una secuencia de numeros
print z[:9]

s="<any strings>"
print s[:3]+s[3:]


os= 'My book is amazing in all the moon'
print os.find('moon')
print os[30:]

s= '<any sting>'
print s.find("")

                                    #FINAL QUIZ

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')
z= page.find('"', start_link)
f= page.find('"',z+1)
url= page[z + 1:f]
print url

print start_link

