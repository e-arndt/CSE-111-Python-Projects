# Author: Eric Arndt
# Class: CSE 111 W02 TEAM Project Can Storage Efficiency
# Calculate volume of can, then calculate efficiency
# Display results to user.

# Import modules
import os
import math


can_data_path              = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\CSE 111\\W02\\TEAM cans\\Can-Data.txt"


# Set static variables
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "CAN EFFICIENCY CALCULATOR "
result_banner              = "CAN EFFICIENCY RESULTS "
text                       = 'Test'
run                        = "Y"
pi                         = math.pi
can_size_data              = []
can_volume_data            = []
can_surface_data           = []
can_efficiency_data        = []



# Set function for clearing terminal screen
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


def read_can_data():
    with open(can_data_path, "r") as can_data:

        # Read the first line of data from the file and store in the variable "header" then move to the next line of data
        header = next(can_data)

        # Loop to step through each line of data in the file
        for can in can_data:
            # Strip off whitespaces in data string
            can_record  = can.strip()
            # Split string of data into separate parts by looking for a ","
            can_record  = can.split(",")
            # Assign variables to each part of the split data
            can_name    = can_record[0]
            can_radius  = float(can_record[1])
            can_height  = float(can_record[2])
            can_cost    = float(can_record[3])

            can_record_data = (f"{can_name}, {can_radius}, {can_height}, {can_cost}")

            can_size_data.append(can_record_data)

                

# Set main function
def main():
    read_can_data()
    compute_volume()
    compute_surface_area()
    compute_efficiency()
    disply_results()


    


def compute_volume():
    for can in can_size_data:
        # Strip off whitespaces in data string
        can_record  = can.strip()
        # Split string of data into separate parts by looking for a ","
        can_record  = can.split(",")
        # Assign variables to each part of the split data
        can_name    = can_record[0]
        can_radius  = float(can_record[1])
        can_height  = float(can_record[2])
        can_cost    = float(can_record[3])

        volume = (pi*can_radius**2*can_height)

        can_volume = (f"{can_name}, {can_radius}, {can_height}, {volume}, {can_cost}")

        can_volume_data.append(can_volume)

        


def compute_surface_area():
    for can in can_volume_data:
        # Strip off whitespaces in data string
        can_record  = can.strip()
        # Split string of data into separate parts by looking for a ","
        can_record  = can.split(",")
        # Assign variables to each part of the split data
        can_name    = can_record[0]
        can_radius  = float(can_record[1])
        can_height  = float(can_record[2])
        can_volume  = float(can_record[3])
        can_cost    = float(can_record[4])

        surface_area = (2*pi*can_radius)*(can_radius+can_height)

        can_surface = (f"{can_name}, {can_radius}, {can_height}, {can_volume}, {surface_area}, {can_cost}")

        can_surface_data.append(can_surface)



def compute_efficiency():
    for can in can_surface_data:
        # Strip off whitespaces in data string
        can_record  = can.strip()
        # Split string of data into separate parts by looking for a ","
        can_record  = can.split(",")
        # Assign variables to each part of the split data
        can_name    = can_record[0]
        can_radius  = float(can_record[1])
        can_height  = float(can_record[2])
        can_volume  = float(can_record[3])
        can_surface = float(can_record[4])
        can_cost    = float(can_record[5])

        storage_efficiency = (can_volume/can_surface)

        can_efficiency = (f"{can_name}, {can_radius}, {can_height}, {can_volume}, {can_surface}, {storage_efficiency}, {can_cost}")

        can_efficiency_data.append(can_efficiency)



def disply_results():
    for can in can_efficiency_data:
        # Strip off whitespaces in data string
        can_record     = can.strip()
        # Split string of data into separate parts by looking for a ","
        can_record     = can.split(",")
        # Assign variables to each part of the split data
        can_name       = can_record[0]
        can_radius     = float(can_record[1])
        can_height     = float(can_record[2])
        can_volume     = float(can_record[3])
        can_surface    = float(can_record[4])
        can_efficiency = float(can_record[5])
        can_cost       = float(can_record[6])

        can_eff = (f"{can_efficiency:.2f}")

        display = (f"NAME: {can_name:<12}  EFFICIENCY: {can_eff:^5}  COST: ${can_cost:<8}")

        print(display)
        

 # Call Clear Screen function
clrscr()
welcome()
main()
print(new_line)
