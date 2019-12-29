# This program asks the user to enter a integer
# then it displays the absolute value of the 
# aforementioned integer to the user

x=int(input("Type a value: "))

def absolute_value(x):
  if x<0:
    return(-x)
  else:
    return(x)
  
print("absolute value: |",x,"| = ", end="")
absolute_value(x)
  
  
##################
##### Output #####
##################

Type a value: -6
absolute value: | -6 | = 6
