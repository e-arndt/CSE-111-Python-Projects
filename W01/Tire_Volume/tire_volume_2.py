# Author: Eric Arndt
# Class: CSE 111 W01 Tire Volume Calculator
# Request tire measurements from user.
# Display calculated data to user.
# Store the date of purchase, tire size data in a text file named "volumes.txt"

# CREATIVITY:
# Clear terminal screen and add a banner at the top.
# Save the DAY, DATE and TIME to the text file. Also include WIDTH, ASPECT RATIO, DIAMETER, VOLUME and PHONE labels to the file.
# Ask if user wants to purchase the tire and if they do, ask for their phone number, save phone number to the text file.
# Ask user if they would like to run the program again or exit the program.

import os
import math
import datetime

# Dictionary of different tire sizes and their prices available for search and/or purchase
tire_prices = {"18560": "119", "18565": "125", "18570": "135", "19560": "142", "19565": "144", "19570": "159", "20560": "165", "20565": "172", "20570": "175", "21560": "179", "21565": "184", "21570": "192", "22560": "195", "22565": "198", "22570": "209", "23560": "215", "23565": "220", "23570": "224", "23575": "249"}

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
tire_volume             = 0
pi                      = math.pi
today                   = datetime.datetime.now()
date                    = 0
step1                   = 0
step2                   = 0
step3                   = 0
step4                   = 0
buy                     = 0
phone                   = 0
run                     = "Y"
stay                    = "N"
user_inquiry            = []
user_data               = []

# Define the file path to use for the text file that will store purchases and customer phone numbers
path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\CSE 111\\W01\\Tire_Volume\\volumes.txt"

# Run the program as long as the While statement is True
while run == "Y" or run == "y":

# Set function for clearing terminal screen
    def clrscr():
            # Check if Operating System is Mac and Linux
            if os.name == 'posix':
                _ = os.system('clear')
            else:
            # Else Operating System is Windows (os.name = nt)
                _ = os.system('cls')

    # Call the clear terminal screen function
    clrscr()

    # Print "Welcome" Banner
    print(red_bg + welcome_banner.center(50,' ') + normal + new_line)

    # Request measurement inputs from user.
    width    = int(input('Enter width of tire in mm (ex 205): '))
    aspect   = int(input('Enter aspect ratio of tire (ex 60): '))
    diameter = int(input('Enter diameter of tire in inches (ex 15): '))

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
    step1       = (width*aspect+2540*diameter)
    # step2 = calculate operation before parentheses 
    step2       = (pi*width**2*aspect)
    # step4 = set variable to the value of the denominator
    step4       = 10000000000
    # step3 = multiply formula outside parentheses with formula inside
    step3       = step2*(step1)
    # volume = result from step3 divided by denominator (step4)
    volume      = step3/step4
    tire_volume = round(volume, 2)
    # Find the current day, date and time
    date        = today.strftime("%a %x %I:%M%p")
    user_data   = str(width) + str(aspect)
    

    # Display approximate volume of tire in liters to user
    print()
    print(f"Approximate tire volume: {tire_volume} liters.")
    print()
    print(f"Price per tire: ${tire_prices[user_data]}.99")
    print()

    # Ask user if they want to purchase the tire shown in the calculated result
    buy = (input('Purchase this tire? [Y/N]: '))
    # If they answer yes also ask for their phone number and store the date, time, tire info and phone number in a text file
    if (buy == "Y" or buy == "y"):
        phone = (input('Please enter your phone number '))
        with open(path, "a") as user_inquiry:
            user_inquiry.write ("Date: " + date + " Width:" + str(width) + "mm" + " Aspect Ratio:" + str(aspect) + " Diameter:" + str(diameter) + " inches" + " Volume:" + str(tire_volume) + " liters" + " Phone:" + str(phone) + new_line)
        print()
    # If they don't want to purchase the tire, store the tire calculation info and the day, date and time in the text file
    elif (buy != "Y" or buy != "y"):
        with open(path, "a") as user_inquiry:
            user_inquiry.write ("Date: " + date + " Width:" + str(width) + "mm" + " Aspect Ratio:" + str(aspect) + " Diameter:" + str(diameter) + " inches" + " Volume:" + str(tire_volume) + " liters" + new_line)
        print()

    # Ask user if they want to run program again
    stay = (input('Run Again? [Y/N]: '))
    if (stay == "Y" or stay == "y"):
        run = "Y"

    elif (stay != "Y" or stay != "y"):
        clrscr()
        run = "N"
