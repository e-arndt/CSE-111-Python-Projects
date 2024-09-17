# Author: Eric Arndt
# Class: CSE 111 W01 Tire Volume Calculator
# Request tire measurements from user.
# Display calculated data to user.

import os
import math

# Set static variables
new_line                = '\n'
esc                     = '\x1b'
red_bg                  = esc + '[41m'
normal                  = esc + '[0m'
welcome_banner          = "TIRE VOLUME CALCULATOR "
width                   = 0
aspect                  = 0
diameter                = 0
volume                  = 0
pi                      = math.pi
step1                   = 0
step2                   = 0
step3                   = 0
step4                   = 0
run                     = "Y"
stay                    = "N"

# While run = yes / y or Y the program runs. Once the user answers no / n or N the While becomes false and the program ends.
while run == "Y" or run == "y":

# Set function for clearing terminal screen
    def clrscr():
            # Check if Operating System is Mac and Linux
            if os.name == 'posix':
                _ = os.system('clear')
            else:
            # Else Operating System is Windows (os.name = nt)
                _ = os.system('cls')

    clrscr()

    # Print "Welcome" Banner
    print(red_bg + welcome_banner.center(50,' ') + normal + new_line)

    # Request measurement inputs from user.
    width    = float(input('Enter width of tire in mm (ex 205): '))
    aspect   = float(input('Enter aspect ratio of tire (ex 60): '))
    diameter = float(input('Enter diameter of tire in inches (ex 15): '))

    # Calculate volume of tire in liters
    # volume = volume of the tire in liters
    # pi = π
    # width = the width of the tire in millimeters
    # aspect = the aspect ratio of the tire
    # diameter = the diameter of the wheel in inches
    # The volume of space inside a tire can be approximated with this formula:
    # v = π w2 a(w a + 2,540 d)
    # -------------------------
    #     10,000,000,000

    # step1 = calculate within parentheses
    step1 = (width*aspect+2540*diameter)
    # step2 = calculate operation before parentheses 
    step2 = (pi*width**2*aspect)
    # step4 = set variable to the value of the denominator
    step4 = 10000000000
    # step3 = multiply formula outside parentheses with formula inside
    step3 = step2*(step1)
    # volume = result from step3 divided by denominator (step4)
    volume = step3/step4

    # Display approximate volume of tire in liters to user
    print()
    print(f"Approximate tire volume: {volume:.2f} liters.")
    print(new_line)

    # Ask user if they want to run program again
    stay = (input('Run Again? [Y/N]: '))
    if (stay == "Y" or stay == "y"):
        run = "Y"

    elif (stay != "Y" or stay != "y"):
        clrscr()
        run = "N"
