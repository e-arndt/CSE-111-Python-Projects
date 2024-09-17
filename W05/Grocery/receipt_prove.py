import csv
import os
import time

dict_path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\CSE 111\\W05\\Grocery\\products.csv"
list_path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\CSE 111\\W05\\Grocery\\request.csv"

# Set static variables
new_line                = '\n'
esc                     = '\x1b'
red_bg                  = esc + '[41m'
normal                  = esc + '[0m'
welcome_banner          = "GROCERY ORDER "


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
    PRODUCT_ID_INDEX      = 0
    PRODUCT_NAME_INDEX    = 1
    PRODUCT_PRICE_INDEX   = 2

    ORDERED_PRODUCT_INDEX = 0
    ORDERED_QTY_INDEX     = 1

    qty_update            = 0

    ordered_items         = []

    # Clear terminal screen
    clrscr()

    # Print welcome banner
    welcome()

    # Read the contents of the students.csv into a
    # compound dictionary named students_dict. Use
    # the phone numbers as the keys in the dictionary.
    products_dict   = read_dictionary(dict_path, PRODUCT_ID_INDEX)

    # Read the text file specified by the user into a list.
    order_requests  = read_list(list_path, ORDERED_PRODUCT_INDEX, ORDERED_QTY_INDEX)
    
    
    print("All Products")
    print(f"{products_dict}")
    print()
    
    
    for order in order_requests:
        
        for product in products_dict:
            print(f" ORDER: {order[ORDERED_PRODUCT_INDEX]}")
            print(f" PROD : {product}")
            if order[ORDERED_PRODUCT_INDEX] == product:
                
                order_item    = products_dict.get(product)

                product_name  = order_item[PRODUCT_NAME_INDEX]
                product_price = order_item[PRODUCT_PRICE_INDEX]
                product_qty   = order[ORDERED_QTY_INDEX]

                item = (f"{product_name}: Qty: {product_qty} @ ${product_price}")

                ordered_items.append(item)
                
                
                
    print("Requested Items")         
        
    for item in ordered_items:
        print(f"{item}")

    print()

    #run = (input("Lookup Another ID? [Y/N]: "))

    #if (run == "Y" or run == "y"):
        #main()

    #elif (run != "Y" or run != "y"):
        #clrscr()
        #end_program()





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
    product_dictionary = {}

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
                product_dictionary[key] = row_list

    # Return the dictionary.
    return product_dictionary



def read_list(filename, product_id_index, product_qty_index):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_lines.
    request_lines = []

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
                product_id  = row_list[product_id_index]
                product_qty = row_list[product_qty_index]
                order_info  = (product_id, product_qty)

                # Store the data from the current
                # row into the dictionary.
                request_lines.append(order_info)

    
    # Return the list that contains the lines of text.
    return request_lines

def end_program():
    exit()

# Call main to start this program.
if __name__ == "__main__":
    main()


