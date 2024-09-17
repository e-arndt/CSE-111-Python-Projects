# Author: Eric Arndt
# Class: CSE 111 W04 Prove: Chemistry
# Request a compound formula and mass of the sample from user. 
# Calculate the molar mass of the molecule and the number of moles 
# in that sample and print the results to the user.

# CREATIVITY: Add dictionary for known chemical formulas.
# Add function named get_formula_name that will display the compound name to user.
# Add terminal screen clearing, mode banners and formatting for a cleaner, easier to read output.
# Ask user if they want to enter another formula or exit the program.
# Some error handling added.


# Import modules
import os
from formula import parse_formula
import sys
import time

# Set static variables
run                        = "Y"
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "MOLAR MASS CALCULATOR "
result_banner              = "MOLAR MASS RESULTS FOR SAMPLE "
periodic_table_dict        = []


# Function for clearing terminal screen
def clrscr():
            # Check if Operating System is Mac and Linux
        if os.name == 'posix':
                _ = os.system('clear')
        else:
            # Else Operating System is Windows (os.name = nt)
                _ = os.system('cls')


# Function to display note about input / parsing limitations
def note():
    clrscr()
    welcome()
    print("NOTE:")
    print("The formula parser doesn't work with all formulas such as ")
    print("Aluminum (AI) or Chlorate (CN−) which has bonded atoms")
    time.sleep(5)
    main()


# Function to display welcome or program main screen banner
def welcome():
        # Print "Welcome" Banner
        print(red_bg + welcome_banner.center(50,' ') + normal + new_line)

# Main function - Has some error handling, gets input from user, calls the parser,
# calls the compound name, calls function that calculates the molar mass, displays results to user,
# askes user if they want to enter another formula or quit the program.
def main():
    clrscr()
    periodic_table = make_periodic_table()
    compound_table = known_molecules_dict
    welcome()
    print("[Example - Ammonium sulphate =  (NH4)2SO4]")
    print("[Example - Calcium hydroxide =    Ca(OH)2]")
    print("[Example - Sodium phosphate  =     Na3PO4]")
    print("[Example - Cellulose         = (C6H10O5)N]")
    print()
    try:
        user_formula   = (input("Please enter a chemical formula: "))
        element_list   = parse_formula(user_formula, periodic_table)
    except:
          print()
          print("Invalid charater or formula not enter correctly. See examples above.")
          time.sleep(3)
          main()
    print()
    sample_size    = float(input("Enter the mass of your sample in grams: "))
    try:
        compound_name  = get_formula_name(user_formula.upper(), compound_table)
    except:
          compound_name = "Unknown Compound"
    
    molar_mass     = compute_molar_mass(element_list,periodic_table)
    sample_moles   = (sample_size) / (molar_mass)
    clrscr()
    print(red_bg + result_banner.center(50,' ') + normal + new_line)
    
    print(f"Compound Name: {compound_name} ")
    print(f"Compound Formula: {user_formula} ")
    print(f"Compound Molar Mass: {molar_mass:.6f} grams/mole")
    print(f"Sample size of {sample_size} grams equals {sample_moles:.6f} moles")
    print(new_line)
    run = (input('Run Again? [Y/N]: '))
    if (run == "Y" or run == "y"):
        clrscr()
        main()

    elif (run != "Y" or run != "y"):
        exit()
        run = "N"
        


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

# Function that calculates the molar mass
def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """

    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    total_molar_mass = 0
    list = symbol_quantity_list
    for item in list:
        element_symbol      = item[SYMBOL_INDEX]
        element_atomic_qty  = item[QUANTITY_INDEX]
        element             = periodic_table_dict[element_symbol]
        element_name        = element[NAME_INDEX]
        element_atomic_mass = element[ATOMIC_MASS_INDEX]
        total_atomic_mass   = (element_atomic_mass * element_atomic_qty)
        total_molar_mass    += total_atomic_mass
        
    
    # Return the total molar mass.
    return total_molar_mass


# Function that searches dictionary of known compound names, returns compound name
# or if not found, returns "unknown".
def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".

    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    molecule_list = known_molecules_dict
    compound = molecule_list[formula]
    if compound == "":
            compound == "Unknown Compound"

    return compound



def make_periodic_table():

        # [symbol, name, atomic_mass]
        periodic_table_dict = {
        "Ac":	["Actinium", 227],
        "Ag":	["Silver", 107.8682],
        "Al":	["Aluminum", 26.9815386],
        "Ar":	["Argon", 39.948],
        "As":	["Arsenic", 74.9216],
        "At":	["Astatine", 210],
        "Au":	["Gold", 196.966569],
        "B":	["Boron", 10.811],
        "Ba":	["Barium", 137.327],
        "Be":	["Beryllium", 9.012182],
        "Bi":	["Bismuth", 208.9804],
        "Br":	["Bromine", 79.904],
        "C":	["Carbon", 12.0107],
        "Ca":	["Calcium", 40.078],
        "Cd":	["Cadmium", 112.411],
        "Ce":	["Cerium", 140.116],
        "Cl":	["Chlorine", 35.453],
        "Co":	["Cobalt", 58.933195],
        "Cr":	["Chromium", 51.9961],
        "Cs":	["Cesium", 132.9054519],
        "Cu":	["Copper", 63.546],
        "Dy":	["Dysprosium", 162.5],
        "Er":	["Erbium", 167.259],
        "Eu":	["Europium", 151.964],
        "F":	["Fluorine", 18.9984032],
        "Fe":	["Iron", 55.845],
        "Fr":	["Francium", 223],
        "Ga":	["Gallium", 69.723],
        "Gd":	["Gadolinium", 157.25],
        "Ge":	["Germanium", 72.64],
        "H":	["Hydrogen", 1.00794],
        "He":	["Helium", 4.002602],
        "Hf":	["Hafnium", 178.49],
        "Hg":	["Mercury", 200.59],
        "Ho":	["Holmium", 164.93032],
        "I":	["Iodine", 126.90447],
        "In":	["Indium", 114.818],
        "Ir":	["Iridium", 192.217],
        "K":	["Potassium", 39.0983],
        "Kr":	["Krypton", 83.798],
        "La":	["Lanthanum", 138.90547],
        "Li":	["Lithium", 6.941],
        "Lu":	["Lutetium", 174.9668],
        "Mg":	["Magnesium", 24.305],
        "Mn":	["Manganese", 54.938045],
        "Mo":	["Molybdenum", 95.96],
        "N":	["Nitrogen", 14.0067],
        "Na":	["Sodium", 22.98976928],
        "Nb":	["Niobium", 92.90638],
        "Nd":	["Neodymium", 144.242],
        "Ne":	["Neon", 20.1797],
        "Ni":	["Nickel", 58.6934],
        "Np":	["Neptunium", 237],
        "O":	["Oxygen", 15.9994],
        "Os":	["Osmium", 190.23],
        "P":	["Phosphorus", 30.973762],
        "Pa":	["Protactinium", 231.03588],
        "Pb":	["Lead", 207.2],
        "Pd":	["Palladium", 106.42],
        "Pm":	["Promethium", 145],
        "Po":	["Polonium", 209],
        "Pr":	["Praseodymium", 140.90765],
        "Pt":	["Platinum", 195.084],
        "Pu":	["Plutonium", 244],
        "Ra":	["Radium", 226],
        "Rb":	["Rubidium", 85.4678],
        "Re":	["Rhenium", 186.207],
        "Rh":	["Rhodium", 102.9055],
        "Rn":	["Radon", 222],
        "Ru":	["Ruthenium", 101.07],
        "S":	["Sulfur", 32.065],
        "Sb":	["Antimony", 121.76],
        "Sc":	["Scandium", 44.955912],
        "Se":	["Selenium", 78.96],
        "Si":	["Silicon", 28.0855],
        "Sm":	["Samarium", 150.36],
        "Sn":	["Tin", 118.71],
        "Sr":	["Strontium", 87.62],
        "Ta":	["Tantalum", 180.94788],
        "Tb":	["Terbium",	158.92535],
        "Tc":	["Technetium", 98],
        "Te":	["Tellurium", 127.6],
        "Th":	["Thorium",	232.03806],
        "Ti":	["Titanium", 47.867],
        "Tl":	["Thallium", 204.3833],
        "Tm":	["Thulium", 168.93421],
        "U":	["Uranium", 238.02891],
        "V":	["Vanadium", 50.9415],
        "W":	["Tungsten", 183.84],
        "Xe":	["Xenon", 131.293],
        "Y":	["Yttrium", 88.90585],
        "Yb":	["Ytterbium", 173.054],
        "Zn":	["Zinc", 65.38],
        "Zr":	["Zirconium", 91.224]
        }

        element_table = periodic_table_dict.copy()

        return element_table





known_molecules_dict = {
"HCL":		"Hydrochloric acid",
"CH3COOH":	"Acetic acid",
"H2SO4":	"Sulfuric acid",
"NH3":		"Ammonia",
"F2":       "Fluorine Gas",
"CASO42H2O":"Calcium Sulphate",
"CH3COO":	"Acetate",
"C3H8O": 	"Isopropyl alcohol",
"C3H8": 	"Propane",
"H3PO4":	"Phosphoric acid",
"C2H6O2":	"Ethylene glycol",
"MGCO3":	"Magnesium carbonate",
"HNO3":		"Nitric acid",
"LIBR":		"Lithium bromide",
"LI3PO4":   "Lithium phosphate",
"LI2O":		"Lithium oxide",
"NA3PO2":	"Sodium hypophosphite",
"NA3PO4":	"Sodium phosphate",
"CACO3":	"Calcium carbonate",
"(NH4)2SO4":"Ammonium sulphate",
"H2CO3":	"Carbonic acid",
"NAHCO3":	"Sodium bicarbonate",
"NAOH":		"Sodium hydroxide",
"CA(OH)2":	"Calcium hydroxide",
"C2H5OH":	"Ethanol",
"C2H6O":	"Ethanol",
"HBR":		"Hydrobromic acid",
"HNO2":		"Nitrous acid",
"KOH":		"Potassium hydroxide",
"AGNO3":	"Silver nitrate",
"NA2CO3":	"Sodium carbonate",
"NACL":		"Sodium chloride",
"(C6H10O5)N":"Cellulose",
"MG(OH)2":	"Magnesium hydroxide",
"CH4":		"Methane",
"HE":		"Helium",
"NO2":		"Nitrogen dioxide",
"N2":		"Nitrogen",
"NANO3":	"Sodium nitrate",
"H2SO3":	"Sulphurous acid",
"AL2(SO4)3":"Aluminium sulphate",
"AL2O3":	"Aluminium oxide",
"NH4NO3":	"Ammonium nitrate",
"(NH4)3PO4":"Ammonium phosphate",
"BA(OH)2":	"Barium hydroxide",
"CCL4":		"Carbon tetrachloride",
"C6H8O7":	"Citric acid",
"HCN":		"Hydrocyanic acid",
"C7H6O3":	"Salicylic acid",
"HI":		"Hydroiodic acid",
"HCLO":		"Hypochlorous acid",
"CH3(CH2)6CH3": "Octane",
"C13H18O2": "Ibuprofen",
"C13H16N2O2": "Melatonin",
"FE2O3":	"Iron(iii) oxide",
"MG3(PO4)2":"Magnesium phosphate",
"C2H3NAO2":	"Sodium acetate",
"NA2SO4":	"Sodium sulphate",
"C12H22O11":"Sucrose",
"KNO3":		"Potassium nitrate",
"NH4HCO3":	"Ammonium bicarbonate",
"NH4CL":	"Ammonium chloride",
"NH4OH":	"Ammonium hydroxide",
"CA(NO3)2":	"Calcium nitrate",
"CAO":		"Calcium oxide",
"CO":		"Carbon monoxide",
"CL2":		"Chlorine gas",
"C6H6O":	"Phenol",
"H2":		"Hydrogen",
"H2O2":		"Hydrogen peroxide",
"OH-":		"Hydroxide",
"MGCL2":	"Magnesium chloride",
"KCL":		"Potassium chloride",
"KI":		"Potassium iodide",
"SO2":		"Sulphur dioxide",
"C3H8O3":	"Glycerin",
"BA(NO3)2":	"Barium nitrate",
"C4H6O4CA":	"Calcium acetate",
"FE2O3":	"Iron oxide",
"K2CO3":	"Potassium carbonate",
"AGCL":		"Silver chloride",
"NAI":		"Sodium iodide",
"NA2O":		"Sodium oxide",
"NA2S":		"Sodium sulphide",
"ZN(NO3)2":	"Zinc nitrate",
"C20H14O4":	"Phenolphthalein",
"MG(NO3)2":	"Magnesium nitrate",
"FeS2": 	"Iron pyrite",
"H2O": 		"Water",
"SIO2":		"Silicon dioxide",
"C3H6O":	"Acetone",
"C6H6O2":	"Hydroquinone",
"C6H14": 	"Hexane",
"C8H18": 	"Octane",
"C5H5N":	"Pyridine",
"C2H3O2NH4":"Ammonium acetate",
"C8H10":	"Xylene",
"BASO4":	"Barium sulphate",
"C6H6":		"Benzene",
"C4H10":	"Butane",
"CHO3-":	"Bicarbonate",
"CRO42-":	"Chromate",
"C4H8O":	"Methyl Ethyl Ketone",
"C2HCL3O2":	"Trichloroacetic acid",
"MGSO4":	"Magnesium sulphate",
"CH3OH":	"Methanol",
"O":		"Oxygen",
"C16H18CLN3S":	"Methylene blue",
"NA2SO3":	"Sodium sulfite",
"SO3":		"Sulphur trioxide",
"ALPO4":	"Aluminium phosphate",
"C18H36O2":	"Stearic acid",
"N2O":		"Dinitrogen monoxide",
"TIO2":		"Titanium dioxide",
"C2H3N":	"Acetonitrile",
"H2C2O4":	"Oxalic acid",
"K2CR2O7":	"Potassium dichromate",
"NABR":		"Sodium bromide",
"NACLO":	"Sodium hypochlorite",
"C4H6O4ZN":    "Zinc acetate"
}

# Function to clear screen and exit the program
def exit():
      clrscr()
      sys.exit(0)


# Check if the program is being imported or executed as a script
if __name__ == "__main__":
    note()