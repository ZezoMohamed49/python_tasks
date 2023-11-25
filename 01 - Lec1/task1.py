
'''
Task1
1 - To count number 4 in a given list.
2 - vowel character.
3 - Environment variables.
'''

############################################ To count number 4 in a given list. #############################################
# Get the input from the user as a string
user_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of strings
numbers_as_strings = user_input.split()

print("Number of fours : {}".format(numbers_as_strings.count("4")))

