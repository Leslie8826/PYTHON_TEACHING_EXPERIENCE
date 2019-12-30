# OPERATION 1 

# This program deletes an element from a list
# with pop method

t = ['a', 'b', 'c']
print("List: \n", t)
x = t.pop(1)
print("\n List after pop operation on element 1: \n", t)
print ("\n Element 1 removed from list: \n", x)


##################
##### Output #####
##################
List: 
 ['a', 'b', 'c']

 List after pop operation on element 1: 
 ['a', 'c']

 Element 1 removed from list: 
 b

 
 
 
# OPERATION 2
# This program deletes an element from a list
# with the del method
 h = ['a', 'b', 'c']
print("List: \n", h)
del h[1]
print("\n List after applying del method on element 1: \n", h)

##################
##### Output #####
##################
List: 
 ['a', 'b', 'c']

 List after applying del method on element 1: 
 ['a', 'c']
 
 
 
 
 
 # OPERATION 3
 # This program removes an element from a list
 d = ['a', 'b', 'c']
print("List: \n", d)
d.remove('b')
print("\n List after removing element b: \n", d)


##################
##### Output #####
##################
List: 
 ['a', 'b', 'c']

 List after removing element b: 
 ['a', 'c']

 
 
 
 # OPERATION 4
 t = ['a', 'b', 'c', 'd', 'e', 'f']
print("List: \n", t)
del t[1:5]
print("\n List after deleting several elements: \n", t)

##################
##### Output #####
##################
List: 
 ['a', 'b', 'c', 'd', 'e', 'f']

 List after deleting several elements: 
 ['a', 'f']

 

