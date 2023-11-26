
'''
Task1
1 - To count number 4 in a given list.
2 - vowel character.
3 - Environment variables.
'''

############################################ To count number 4 in a given list. #############################################
# Get the input from the user as a string
#user_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of strings
#numbers_as_strings = user_input.split()

#print("Number of fours : {}".format(numbers_as_strings.count("4")))

################################################### Vowel character check ###################################################
#vowel_set = {'A','E','I','O','U'}
#user_input = input("Enter a character: ")
#print("The character you entered is vowel") if user_input.upper() in vowel_set else print("The character you entered is consonant")


################################################### Environment variables ####################################################
import os

# Get the value of an environment variable
value = os.environ['PATH'].split(";")
for i in value :
    print(i)


