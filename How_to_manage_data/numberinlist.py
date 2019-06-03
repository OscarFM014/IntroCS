# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    final = []
    lista = []
    contador = 0
    inicio = 0
    while True:
        contador = contador + 1
        final.append(int(string[inicio])) #Agrego el primer número
        if contador == (len(string)):
            return final
        while int(string[inicio]) >= int(string[contador]):
            lista.append(int(string[contador]))
            contador = contador + 1
            if contador == (len(string)):
                final.append(lista)
                return final
        inicio = contador
        if len(lista) == 0:
            final = final
        else:
            final.append(lista)
        lista = []





#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print (repr(string), numbers_in_lists(string) == result)
string = '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print (repr(string), numbers_in_lists(string) == result)
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print (repr(string), numbers_in_lists(string) == result)
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (repr(string), numbers_in_lists(string) == result)
