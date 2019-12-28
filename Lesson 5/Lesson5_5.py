# This program uses a function that takes 2 arguments
# and print each one of them side by side

def cat_twice(line1, line2):
  print(line1, end="")
  print(line2)

line1 = 'This is'
line2 = ' a test'

print("the 1st line is: ", line1, end="")
print("\nthe 2nd line is: ", line2, end="")
print("\n")
cat_twice(line1, line2)



##################
##### Output #####
##################

the 1st line is:  This is
the 2nd line is:   a test

This is a test
