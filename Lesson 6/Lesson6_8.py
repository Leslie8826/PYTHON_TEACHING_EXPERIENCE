# This program uses recursion to countdown numbers from 10 one by one.
# Once 0 is reached, the program prints 'Blastoff!'

n = 10

def countdown(n):
  if n <= 0:
    print('Blastoff!') 
  else:
    print(n)
    countdown(n-1)
    
countdown(n)


##################
##### Output #####
##################
10
9
8
7
6
5
4
3
2
1
Blastoff!
