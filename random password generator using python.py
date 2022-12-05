 Importing the necessary modules

import random #This will perform random generations
import string #The string module contains a number of useful constants, classes and a number of functions

print('Hello. This is a random password generator.\n')

length = int(input('Enter the length of the password you want: '))
if length>12:

    lower_case = string.ascii_lowercase # All lower .case letters
    upper_case = string.ascii_uppercase # All Upper case letters
    numerals = string.digits # String will contain digits from 0 to 9
    characters = string.punctuation # The special characters

# Joining all of the above data
    all = lower_case + upper_case + numerals + characters

# Using random module to generate the characters
    Generate = random.sample(all,length)

# Creating the password    
    password = "".join(Generate)

#Replacing the unwanted Characters
    pp=(password.replace('<',']') and password.replace('>','['))

#Printing the password
    print(pp)
else:
    print("Enter a valid length")
