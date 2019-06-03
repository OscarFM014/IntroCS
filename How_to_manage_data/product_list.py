# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    """z = (len(list_of_numbers))-1
    contador = 0
    if z > 1:
        while z > 0:
            contador = list_of_numbers[z] * list_of_numbers[z-1]
            list_of_numbers.pop()
            list_of_numbers.pop()
            list_of_numbers.append(contador)
            z = z - 1
        return (list_of_numbers[0])
    else:
        if z == 0:
            return list_of_numbers[0]
    return 1"""
    total = 1
    for i in list_of_numbers:
        total = total * i
    return total


print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([0.5,0.5])
#>>> 1
