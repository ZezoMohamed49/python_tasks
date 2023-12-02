'''
Task1
Favorite websites
'''
import chromelink

print("For facebook press 0\nFor google press   1\nFor linkedin press 2")
choice = int(input("Enter you option : "))                      # ask the user to select which link to run.

if choice in range(0,3):                                        # Check if the user input from 0 -> 2
    chromelink.open_link(chromelink.links[choice])              # Open the link.
else :
    print("Wrong option!!!")