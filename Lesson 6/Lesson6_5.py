# This program asks the user to enter a temperature.
# Then the program checks the value entered by the user
# and print a message according to the value of the temperature entered

temperature = int(input("What is the temperature today? "))

if (temperature > 0):
  print('This is a great day')
else:
  print('Stay home')

  

##################
##### Output #####
##################
#output 1
What is the temperature today? -25
Stay home

#output 2
What is the temperature today? 95
This is a great day
