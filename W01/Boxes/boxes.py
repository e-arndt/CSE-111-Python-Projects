# Author: Eric Arndt
# Class: CSE 111 W02 Box Packing Calculator
# Request number of items and number of items per box from user.
# Display calculated data to user.
# Added a function to clear the terminal screen for a cleaner look
# Added a top banner to identify the purpose of the program
# Added the option for the user to run the program again or to exit


# import the OS and math modules
# OS used in checking what operating system is being used
import os
# Used for additional mathmatical functions
import math

# Set static variables
new_line                = '\n'
esc                     = '\x1b'
red_bg                  = esc + '[41m'
normal                  = esc + '[0m'
welcome_banner          = "BOX PACKING CALCULATOR "
num_items               = 0
items_per_box           = 0
num_boxes               = 0
run                     = "Y"
stay                    = "N"
while run == "Y" or run == "y":

# Set function for clearing terminal screen
    def clrscr():
            # Check if Operating System is Mac and Linux
            if os.name == 'posix':
                _ = os.system('clear')
            else:
            # Else Operating System is Windows (os.name = nt)
                _ = os.system('cls')

    # Call the clrscr function to clear the terminal screen
    clrscr()

    # Print "Welcome" Banner
    print(red_bg + welcome_banner.center(50,' ') + normal + new_line)

    # Request item inputs from user.
    num_items     = int(input('Enter total number of items: '))
    items_per_box = int(input('Enter number of items per box: '))

    # Calculate number of boxes required based on total number of items
    # and the number of items allowed per box.
    # Use math.ceil to calculate the next higher integer (ex 6.25 boxes becomes 7 whole boxes)
    num_boxes = math.ceil(num_items/items_per_box)

    # Display required number of boxes to user
    print()
    print(f"For {num_items} items, packing {items_per_box} items per box,")
    print(f"you will need a total of {num_boxes} boxes.")
    print(new_line)

    # Ask user if they want to run program again
    stay = (input('Run Again? [Y/N]: '))
    if (stay == "Y" or stay == "y"):
        run = "Y"

    elif (stay != "Y" or stay != "y"):
        clrscr()
        run = "N"
