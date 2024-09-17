# Author: Eric Arndt
# Class: CSE 111 W03 Prove Project - Water Flow
# Calculate delivered water pressure based on user inputs
# Display results to user.

# CREATIVITY: Assigned constants to be used in formula calculations 
# rather than typed numeric values in each formula
# Added a function to convert from kPA to psi
# Added a test function for the kPa to psi function
# Added terminal screen clearing and banners for a cleaner, easier to read output

# Import OS module used to check which OS is in use
import os

# Set static variables
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "CALCULATE DELIVERED WATER PRESSURE "
result_banner              = "DELIVERED WATER PRESSURE RESULTS "


# Function for clearing the terminal screen
def clrscr():
            # Check if Operating System is Mac and Linux
        if os.name == 'posix':
                _ = os.system('clear')
        else:
            # Else Operating System is Windows (os.name = nt)
                _ = os.system('cls')

# Function to display a banner that describes the purpose or function of the proogram / current screen
def welcome():
          # Print "Welcome" Banner
        print(red_bg + welcome_banner.center(50,' ') + normal + new_line)

# Function to calculate the height of the water column based on height of the water tower 
# and the height of the water tank on top of the tower
def water_column_height(tower_height, tank_height):
    wch = tower_height + (3*tank_height / 4)

    return wch

# Function to calculate the pressure gain based on water density, gravity's pull on the water 
# and the tower / tank height
def pressure_gain_from_water_height(height, gravity, density):
    pressure = (density * gravity * height) / 1000

    return pressure

# Function to calculate the loss of pressure based on pipe diameter, 
# pipe length, friction, water velocity and density
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity, density):
    ploss = (-friction_factor)*(pipe_length*density*(fluid_velocity**2)) / (2000*pipe_diameter)

    return ploss

# Function to calculate the loss of pressure based on number of pipe fittings, water velocity and density
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings, density):
    floss = ((-0.04*density) * fluid_velocity**2 * quantity_fittings) / 2000

    return floss

# Function that calculates the Reynolds Number to help predict fluid flow 
def reynolds_number(hydraulic_diameter, fluid_velocity, density, viscosity):
    reynolds_num = (density * hydraulic_diameter * fluid_velocity) / viscosity

    return reynolds_num

# Function to calculate the loss of pressure based on changes in pipe diameter, 
# Reynolds Number predictions, water density and velocity
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, density):
    k = (0.1 + 50/reynolds_number) * ((larger_diameter/smaller_diameter)**4 - 1)
    prloss = (-k * density * (fluid_velocity**2)) / 2000

    return prloss

# Function to convert from kPa(kilopascal) to psi(pounds per square inch)
def kPa_psi_conversion(kPa):
    psi_pressure = (kPa * 0.14503773773020923)

    return psi_pressure

# Set variables for pipe diameters, velocities, gravity, density and friction
PVC_SCHED80_INNER_DIAMETER    = 0.28687   # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR   = 0.013     # (unitless)
SUPPLY_VELOCITY               = 1.65      # (meters / second)

HDPE_SDR11_INNER_DIAMETER     = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR    = 0.018     # (unitless)
HOUSEHOLD_VELOCITY            = 1.75      # (meters / second)

EARTH_ACCELERATION_OF_GRAVITY = 9.80665   # (meters / second²)
WATER_DENSITY                 = 998.2     # (kilograms / meter³)
WATER_DYNAMIC_VISCOSITY       = 0.0010016 # (Pascal seconds)


# Main function that controls user inputs and execution of 
# other functions to calculated and display the desired output.
def main():
    # call clear terminal screen function
    clrscr()
    # Display the "Welcome" banner
    welcome()
    # Collect user inputs
    tower_height    = float(input("Height of water tower (meters): "))
    tank_height     = float(input("Height of water tank walls (meters): "))
    length1         = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2         = float(input("Length of pipe from supply to house (meters): "))

    # Assign shorter variable names to the preset values
    diameter     = PVC_SCHED80_INNER_DIAMETER
    friction     = PVC_SCHED80_FRICTION_FACTOR
    velocity     = SUPPLY_VELOCITY
    gravity      = EARTH_ACCELERATION_OF_GRAVITY
    density      = WATER_DENSITY
    viscosity    = WATER_DYNAMIC_VISCOSITY

    # Call the functions in proper order required to calculate the delivered water pressure
    # Store the calculated results in variables
    water_height = water_column_height(tower_height, tank_height)
    pressure     = pressure_gain_from_water_height(water_height, gravity, density)
    reynolds     = reynolds_number(diameter, velocity, density, viscosity)
    loss         = pressure_loss_from_pipe(diameter, length1, friction, velocity, density)
    pressure += loss

    loss         = pressure_loss_from_fittings(velocity, quantity_angles, density)
    pressure += loss

    loss         = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER, density)
    pressure += loss

    diameter     = HDPE_SDR11_INNER_DIAMETER
    friction     = HDPE_SDR11_FRICTION_FACTOR
    velocity     = HOUSEHOLD_VELOCITY
    loss         = pressure_loss_from_pipe(diameter, length2, friction, velocity, density)
    pressure += loss

    # Call the kPa to psi convert function
    psi = kPa_psi_conversion(pressure)
    # Clear the terminal screen
    clrscr()
    # Display the Result Page banner
    print(red_bg + result_banner.center(50,' ') + normal + new_line)
    # Display the calculated water pressure results in kPa and psi to the user
    print(f"Pressure at house: ")
    print(f"{pressure:.2f} kilopascals or {psi:.2f} psi")
    print(new_line)

# Check if the program is being imported or executed as a script
if __name__ == "__main__":
    main()


