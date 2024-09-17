import os
import sys
import time

run                        = "Y"
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "VEHICLE DATA LOOKUP BY VIN "
result_banner              = "VEHICLE DATA RESULTS "


def clrscr():
            # Check if Operating System is Mac and Linux
        if os.name == 'posix':
                _ = os.system('clear')
        else:
            # Else Operating System is Windows (os.name = nt)
                _ = os.system('cls')


def welcome():
        # Print "Welcome" Banner
        print(red_bg + welcome_banner.center(50,' ') + normal + new_line)


def main():
    clrscr()
    welcome()
    # Create a dictionary that contains data about six vehicles.
    # The key for each vehicle in the dictionary is the vehicle's
    # identification number (VIN). The value for each vehicle is
    # a list that contains the year, manufacturer, model, color,
    # engine design, and engine displacement.
    vehicles_dict = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
    }


    run = ""
    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3

    # Ask the user for a vehicle identification number (VIN).
    vin = input("Please enter a VIN: ")

    # Check if the vin is a key that is in the vehicles dictionary.
    if vin in vehicles_dict:
        # Find the data for the vehicle that the user wants.
        vehicle_info  = vehicles_dict[vin]
        manufacturer  = vehicle_info[MANUFACTURER_INDEX]
        vehicle_model = vehicle_info[MODEL_INDEX]
        vehicle_color = vehicle_info[COLOR_INDEX]

        # Print the manufacturer, model, and color of the vehicle.
        # Don't print the year, engine design, or displacement.
        clrscr()
        print(red_bg + result_banner.center(50,' ') + normal + new_line)
        print(f"VIN: {vin}")
        print(f"Manufacturer : {manufacturer}")
        print(f"Vehicle Model: {vehicle_model}")
        print(f"Vehicle Color: {vehicle_color}")
        print()
        again()
    

    else:
        # Print a message stating that the VIN entered
        # by the user is not in the dictionary.
        print()
        print(f"{vin} is not in the dictionary.")
        print()
        time.sleep(1)
        again()


def again():
    run = (input('Run Again? [Y/N]: '))
    if (run == "Y" or run == "y"):
        clrscr()
        main()

    elif (run != "Y" or run != "y"):
        exit()
        run = "N"


def exit():
      clrscr()
      sys.exit(0)


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
