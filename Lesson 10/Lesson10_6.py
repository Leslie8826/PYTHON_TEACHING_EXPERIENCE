# SLICE 1
# name_of_string[n:m]
# This program slices a list. It returns the part of the list from the “n-eth” character
#  to the “m-eth” character including the first but excluding the last
t = ['a', 'b', 'c', 'd', 'e', 'f']
print("List t: ", t)
print("\n Slice t[1:3] results in: ")
t[1:3]

##################
##### Output #####
##################
List t:  ['a', 'b', 'c', 'd', 'e', 'f']

 Slice t[1:3] results in: 
['b', 'c']




# SLICE 2
# name_of_string[:n]
# This program slices a list. It returns the part of the list 
# that is before the the “n-eth” character including the “n-eth” character
t = ['a', 'b', 'c', 'd', 'e', 'f']
print("List t: ", t)
print("\n Slice t[:4] results in: ")
t[:4]

##################
##### Output #####
##################
List t:  ['a', 'b', 'c', 'd', 'e', 'f']

 Slice t[:4] results in: 
['a', 'b', 'c', 'd']




# SLICE 3
# name_of_string[m:]
# This program slices a list. It returns the part of the list 
# that is after the the “m-eth” character including the “m-eth” character
t = ['a', 'b', 'c', 'd', 'e', 'f']
print("List t: ", t)
print("\n Slice t[4:] results in: ")
t[4:]

##################
##### Output #####
##################
List t:  ['a', 'b', 'c', 'd', 'e', 'f']

 Slice t[4:] results in: 
['e', 'f']


