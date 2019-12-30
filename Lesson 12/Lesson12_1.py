# This program creates 2 tuples and swipe them
t = ('a', 'b', 'c')
p = ('v', 'x', 'w')

print('BEFORE SWAPPING:')
print('t = ', end='')
print(t)
print('p = ', end='')
print(p)

t, p = p, t
print('\n AFTER SWAPPING:')
print('t = ', end='')
print(t)
print('p = ', end='')
print(p)




##################
##### Output #####
##################
BEFORE SWAPPING:
t = ('a', 'b', 'c')
p = ('v', 'x', 'w')

 AFTER SWAPPING:
t = ('v', 'x', 'w')
p = ('a', 'b', 'c')
