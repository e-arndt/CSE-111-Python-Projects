import csv
import os
import time

path                    = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\CSE 111\\W05\\Student\\students.csv"


# Set static variables
new_line                = '\n'
esc                     = '\x1b'
red_bg                  = esc + '[41m'
normal                  = esc + '[0m'
welcome_banner          = "STUDENT LOOKUP BY ID# "


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



def main():
    # Index of the ID number column
    # in the students.csv file.
    ID_INDEX = 0

    # Clear terminal screen
    clrscr()

    # Print welcome banner
    welcome()

    # Read the contents of the students.csv into a
    # compound dictionary named students_dict. Use
    # the phone numbers as the keys in the dictionary.
    students_dict   = read_dictionary(path, ID_INDEX)

    student_id_num  = user_input()
    
    student_num_len = (len(student_id_num))

    alpha_check = student_id_num.isnumeric()
    if alpha_check == False:
        print()
        print(f"{student_id_num} is invalid , please enter only numbers")
        time.sleep(4)
        main()
    

    if student_num_len < 9:
        print()
        print(f"Entry is too short. ID must be 9 digits long")
        time.sleep(3)
        main()


    elif student_num_len >= 10:
        print()
        print(f"Entry is too long. ID must be 9 digits long")
        time.sleep(3)
        main()

    

    student_data  = students_dict.get(student_id_num)

    if student_data:
        student_id    = student_data[0]
        student_name  = student_data[1]
        print()
        print(f"Student ID #: {student_id}")
        print(f"Student Name: {student_name}")
        print(new_line)

    else:
        print()
        print(f"Student ID #: {student_id_num} Not Found")
        print(new_line)


    run = (input("Lookup Another ID? [Y/N]: "))

    if (run == "Y" or run == "y"):
        main()

    elif (run != "Y" or run != "y"):
        clrscr()
        end_program()


def user_input():
    clrscr()
    welcome()

    student_num = (input('Enter student ID#: '))

    return student_num



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    student_dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                student_dictionary[key] = row_list

    # Return the dictionary.
    return student_dictionary

def end_program():
    exit()

# Call main to start this program.
if __name__ == "__main__":
    main()


