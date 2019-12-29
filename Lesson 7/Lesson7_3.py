# This program asks the user to enter 3 grades.
# Then the program will average those 3 grades and 
# display them to the user

a = float(input("Your 1st grade: "))
b = float(input("Your 2nd grade: "))
c = float(input("Your 3rd grade: "))

def average(a, b, c):
  return(a+b+c)/3

print() # this is a space
print("average = ", end="")
average(a, b, c)




##################
##### Output #####
##################

Your 1st grade: 95.7
Your 2nd grade: 99.3
Your 3rd grade: 92.5

average = 95.83333333333333
