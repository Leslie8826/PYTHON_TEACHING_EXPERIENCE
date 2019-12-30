# This program creates a list with 2 elements
# and replaces one of the 2 elements with a new element.
# It prints the new list.
# The program also checks if an element is in the list.

numbers = [42, 105]

print('List')
print('numbers = ', end="")
print(numbers)
print('\n')

print('List after changing second value: ')
numbers[1] = -3
print('numbers = ', end='')
print(numbers)
print('\n')

print('Is 8 a value of the list?')
8 in numbers



##################
##### Output #####
##################
List
numbers = [42, 105]

List after changing second value: 
numbers = [42, -3]

Is 8 a value of the list?
False
