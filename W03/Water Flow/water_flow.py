import os

# Set static variables
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "CALCULATE DELIVERED WATER PRESSURE "
result_banner              = "DELIVERED WATER PRESSURE RESULTS "



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


def water_column_height(tower_height, tank_height):
    wch = tower_height + (3*tank_height / 4)

    return wch


def pressure_gain_from_water_height(height, gravity, density):
    pressure = (density * gravity * height) / 1000

    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity, density):
    ploss = (-friction_factor)*(pipe_length*density*(fluid_velocity**2)) / (2000*pipe_diameter)

    return ploss


def kPa_psi_conversion(kPa):
    psi_pressure = (kPa * 0.14503773773020923)

    return psi_pressure


PVC_SCHED80_INNER_DIAMETER    = 0.28687   # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR   = 0.013     # (unitless)
SUPPLY_VELOCITY               = 1.65      # (meters / second)

HDPE_SDR11_INNER_DIAMETER     = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR    = 0.018     # (unitless)
HOUSEHOLD_VELOCITY            = 1.75      # (meters / second)

EARTH_ACCELERATION_OF_GRAVITY = 9.80665   # (meters / second²)
WATER_DENSITY                 = 998.2     # (kilograms / meter³)




def main():
    clrscr()
    welcome()
    tower_height    = float(input("Height of water tower (meters): "))
    tank_height     = float(input("Height of water tank walls (meters): "))
    length1         = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2         = float(input("Length of pipe from supply to house (meters): "))

    
    diameter     = PVC_SCHED80_INNER_DIAMETER
    friction     = PVC_SCHED80_FRICTION_FACTOR
    velocity     = SUPPLY_VELOCITY
    gravity      = EARTH_ACCELERATION_OF_GRAVITY
    density      = WATER_DENSITY
    

    water_height = water_column_height(tower_height, tank_height)
    pressure     = pressure_gain_from_water_height(water_height, gravity, density)
    loss         = pressure_loss_from_pipe(diameter, length1, friction, velocity, density)
    pressure += loss

    diameter     = HDPE_SDR11_INNER_DIAMETER
    friction     = HDPE_SDR11_FRICTION_FACTOR
    velocity     = HOUSEHOLD_VELOCITY
    loss         = pressure_loss_from_pipe(diameter, length2, friction, velocity, density)
    pressure += loss


    psi = kPa_psi_conversion(pressure)
    clrscr()
    print(red_bg + result_banner.center(50,' ') + normal + new_line)
    print(f"Pressure at house: ")
    print(f"{pressure:.2f} kilopascals or {psi:.2f} psi")
    print(new_line)


if __name__ == "__main__":
    main()


