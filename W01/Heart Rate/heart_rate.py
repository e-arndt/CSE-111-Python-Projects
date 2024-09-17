# Author: Eric Arndt
# Class: CSE 111 W01 Heart Rate Calculator
# Request age from user.
# Display calculated data to user.
# I added a function to clear the terminal screen for a cleaner look
# Added a top banner to identify the purpose of the program
# Added the option for the user to run the program again or to exit

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# import the OS module to use in checking what operating system is being used
import os

# Set static variables
new_line            = '\n'
esc                 = '\x1b'
red_bg              = esc + '[41m'
normal              = esc + '[0m'
welcome_banner      = "HEART RATE CALCULATOR "
age                 = 0
lower_heart_rate    = 0
upper_heart_rate    = 0
max_rate            = 220
run                     = "Y"
stay                    = "N"
while run == "Y" or run == "y":

# Set function for clearing terminal screen based on type of OS
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

    # Request age input from user
    age = int(input('Enter your age: '))

    # Calculate heart rate range by age
    max_rate = (max_rate - age)
    lower_heart_rate = (.65 * max_rate)
    upper_heart_rate = (.85 * max_rate)

    # Display ideal heart rate range for user
    print()
    print("When exercising to strengthen your heart, ")
    print("you should keep your heart rate between")
    print(f"{lower_heart_rate:.0f} and {upper_heart_rate:.0f} beats per minute.")
    print(new_line)

    # Ask user if they want to run program again
    stay = (input('Run Again? [Y/N]: '))
    if (stay == "Y" or stay == "y"):
        run = "Y"

    elif (stay != "Y" or stay != "y"):
        clrscr()
        run = "N"