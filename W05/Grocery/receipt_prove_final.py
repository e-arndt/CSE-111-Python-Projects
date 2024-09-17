# Author: Eric Arndt
# Class: CSE 111 W05 Prove: Grocery Store
# Read request.csv (customer grocery order) match ordered items with products.csv (available products)
# Print store name, display items ordered, calculate subtotal, number of items ordered, sales tax, total,
# a thank you message and time / date. Also include try: except: to handle item not in dictionary and
# data file not found errors.

# CREATIVITY: 
# Add discount for sales on Tue or Wed.
# Add discount for sales before 11:00AM (12:00AM - 10:59:59AM).
# Add function to print coupon on bottom of receipt that randomly picks an item from the current sale,
# coupon also selects a random % OFF between 10% and 50% by tens, ex 10% 20% 30%....
# Add website for survey to bottom of receipt.
# Add terminal screen clearing, formatting and text alignment for a cleaner, easier to read output.

# Import modules
import csv
import os
import sys
import datetime
import random

# Set data files and their path
dict_path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\CSE 111\\W05\\Grocery\\products.csv"
list_path = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\CSE 111\\W05\\Grocery\\request.csv"

# Set static variables
new_line                = '\n'
esc                     = '\x1b'
red_bg                  = esc + '[41m'
normal                  = esc + '[0m'
store_banner          = "FOOD FAIR GROCERY"


# Set function for clearing terminal screen
def clrscr():
    # Check if Operating System is Mac and Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')



# Main function
def main():
    # Index of the ID number column
    # in the students.csv file.
    PRODUCT_ID_INDEX      = 0
    PRODUCT_NAME_INDEX    = 1
    PRODUCT_PRICE_INDEX   = 2

    ORDERED_PRODUCT_INDEX = 0
    ORDERED_QTY_INDEX     = 1

    calc_sub_total        = 0
    sub_total             = 0
    item_count            = 0
    tax_rate              = .06
    disc_rate             = .10

    ordered_items         = []
    ordered_item_name     = []

    # set variable names for date and time
    today     = datetime.datetime.today()
    now       = datetime.datetime.now()
    
    # Format the date and time to read, ex: Wed Jul 03 2024 10:23:45AM
    date_time = now.strftime("%a %b %d %Y %I:%M:%S%p")

    # Clear terminal screen
    clrscr()

    # Read product data file / Error handling for missing file
    try:
        # Read the contents of the students.csv into a
        # compound dictionary named students_dict. Use
        # the phone numbers as the keys in the dictionary.
        products_dict   = read_dictionary(dict_path, PRODUCT_ID_INDEX)

    # Error handling for missing file
    except FileNotFoundError:
        print(f"ERROR: File not found!!")
        print(f"Expected 'products.csv' file at {dict_path}", file=sys.stderr)
        print(new_line) 
        end_program()

    # Error handling for file permission error
    except PermissionError:
        print(f"ERROR: Insufficient permission to read 'products.csv' file")
        print(f"at {dict_path}", file=sys.stderr)
        print(new_line) 
        end_program()

    # Handling for Is A Directory error
    except IsADirectoryError:
        print(f"ERROR: {dict_path} is a directory!", file=sys.stderr)
        print(new_line) 
        end_program()

    # Read order request file / Error handling for missing file
    try:
        # Read the text file specified by the user into a list.
        order_requests  = read_list(list_path, ORDERED_PRODUCT_INDEX, ORDERED_QTY_INDEX)

    # Error handling for missing file
    except FileNotFoundError:
        print(f"ERROR: File not found!!")
        print(f"Expected 'request.csv' file at {list_path}", file=sys.stderr)
        print(new_line) 
        end_program()

    #Error handling for file permission errors
    except PermissionError:
        print(f"ERROR: Insufficient permission to read 'request.csv' file")
        print(f"at {list_path}", file=sys.stderr)
        print(new_line) 
        end_program()
    
    
    # Error handling for bad product code errors
    try:
        for order in order_requests:
            
            # Get product info for products that match products in order requests
            order_item      = products_dict.get(order[ORDERED_PRODUCT_INDEX])
            product_name    = order_item[PRODUCT_NAME_INDEX]
            product_price   = order_item[PRODUCT_PRICE_INDEX]
            product_qty     = order[ORDERED_QTY_INDEX]

            # Construct usuable / printable data string for each item
            item            = (f"{product_name:<22} {product_qty:^2} @  ${product_price:<8}")

            # Calculate subtotal
            calc_sub_total += float(order_item[PRODUCT_PRICE_INDEX]) * int(order[ORDERED_QTY_INDEX])
            # Calculate number of items purchased
            item_count     += (int(order[ORDERED_QTY_INDEX]))
            
            # Append item names to a list for use in randomly picking a product for the coupon
            ordered_item_name.append(product_name)
            # Append the printable data string of ordered items to a list to use in constructing the receipt
            ordered_items.append(item)
            
    # Error message displayed if a product code in the order request is not found in the product list          
    except TypeError:
        print(f"Error: {order[ORDERED_PRODUCT_INDEX]} is an unknown product ID in request.csv file")
        print("Please correct the error and run the file again.") 
        print(new_line) 
        end_program()


    
    # If today id Tue or Wed, apply a 10% discount
    if (today.weekday() == 1 or today.weekday() == 2):
        # Print name of store
        print(red_bg + store_banner.center(40,' ') + normal)      
        print()
        # Print column header names
        print(f"{'       item':<21} {'qty':^4}    {'each'}")
        print('-' * 40)
        # Print each ordered item that was saved to the ordered items list
        for item in ordered_items:
            print(f"{item}")
        print()
        # Calculate the discount. Rounding and limit to 2 digits
        discount = round((calc_sub_total * disc_rate), 2)
        # Calculate the subtotal with the applied discount. Round and limit to 2 digits
        sub_total = round((calc_sub_total - discount), 2)
        # Display total number of items purcased
        print(f"Number of items: {item_count}")
        print()
        # Display type of discount (DAY - Tue / Wed)
        print(f"{'Day Discount:':<10} ${discount}")
        # Display subtoal after applied discount
        print(f"{'Subtotal:':<12} ${sub_total}")
        # Calculate sales tax, round the result and limit to 2 digits
        sales_tax = round((sub_total * tax_rate), 2)
        # Display the sales tax
        print(f"{'Sales Tax:':<13} ${sales_tax}")
        # Calculate the total purchase amount
        total = round((sub_total + sales_tax),2)
        # Display the sales total including tax and any applied discounts
        print(f"{'Total:':<12} ${total}")
        print()
        # Print thank you message
        print(f"Thank You for shopping {store_banner}")
        print()
        # Print date / time
        print(date_time)
        # Call print coupon function
        print_coupon(ordered_item_name)
        print(new_line)


    # If not Tue or Wed, check to see if sale was made before 11am (12:00AM - 10:59:59AM)
    elif now.hour >= 0 and now.hour < 11:
        # Print name of store
        print(red_bg + store_banner.center(40,' ') + normal)      
        print()
        # Print column header names
        print(f"{'       item':<21} {'qty':^4}    {'each'}")
        print('-' * 40)
        # Print each ordered item that was saved to the ordered items list
        for item in ordered_items:
            print(f"{item}")
        print()
        # Calculate the discount. Rounding and limit to 2 digits
        discount = round((calc_sub_total * disc_rate), 2)
        # Calculate the subtotal with the applied discount. Round and limit to 2 digits
        sub_total = round((calc_sub_total - discount), 2)
        # Display total number of items purcased
        print(f"Number of items: {item_count}")
        print()
        # Display type of discount (AM - morning hour) 
        print(f"{'AM Discount:':<10} ${discount}")
        # Display subtoal after applied discount
        print(f"{'Subtotal:':<11} ${sub_total}")
        # Calculate sales tax, round the result and limit to 2 digits
        sales_tax = round((sub_total * tax_rate), 2)
        # Display the sales tax
        print(f"{'Sales Tax:':<12} ${sales_tax}")
        # Calculate the total purchase amount
        total = round((sub_total + sales_tax),2)
        # Display the sales total including tax and any applied discounts
        print(f"{'Total:':<11} ${total}")
        print()
        # Print thank you message
        print(f"Thank You for shopping {store_banner}")
        print()
        # Print date / time
        print(date_time)
        # Call print coupon function
        print_coupon(ordered_item_name)
        print(new_line)


    # If not Tue or Wed and not before 11am (12:00AM - 10:59:59AM), then no discount applies
    else:
        # Print name of store
        print(red_bg + store_banner.center(40,' ') + normal)      
        print()
        # Print column header names
        print(f"{'       item':<21} {'qty':^4}    {'each'}")
        print('-' * 40)
        # Print each ordered item that was saved to the ordered items list
        for item in ordered_items:
            print(f"{item}")
        print()
        # Calculate the subtotal with the applied discount. Round and limit to 2 digits
        sub_total = round(calc_sub_total, 2)
        # Display total number of items purcased
        print(f"Number of items: {item_count}")
        print()
        # Display subtoal after applied discount
        print(f"Subtotal: ${sub_total}")
        # Calculate sales tax, round the result and limit to 2 digits
        sales_tax = round((sub_total * tax_rate), 2)
        # Display the sales tax
        print(f"Sales Tax: ${sales_tax}")
        # Calculate the total purchase amount
        total = round((sub_total + sales_tax),2)
        # Display the sales total including tax and any applied discounts
        print(f"{'Total:':<9} ${total}")
        print()
        # Print thank you message
        print(f"Thank You for shopping {store_banner}")
        print()
        # Print date / time
        print(date_time)
        # Call print coupon function
        print_coupon(ordered_item_name)
        print(new_line)



# Function to print coupon at bottom of receipt. 
# When the fuction is called the file name ordered_item_name is passed to the function to use
def print_coupon(ordered_item_name):
        # List of numbers to be randomly chosen for discount %
        num_list = [10, 10, 15, 15, 20, 25, 30, 35, 40, 45, 50]
        # pick a number randomly from the number list
        num = (random.choice(num_list))
        print()
        # Create a text coupon
        print('-' * 40)
        # Display the randomly picked number for ??% OFF
        print(f"{'|':<10} {'****GET'} {num}% {'OFF****':<16}{'|'}")
        print(f"{'|':<39}{'|'}")
        print(f"{'|':<9} {'YOUR NEXT PURCHASE OF':<29}{'|'}")
        print(f"{'|':<39}{'|'}")
        # Randomly pick the name of one of the products purchased that was stored in the name list
        print(f"{'|':<13} {random.choice(ordered_item_name).upper():<25}{'|'}")
        print('-' * 40)
        print()
        # Print survey website
        print(f"    {'Survey @ www.survey.foodfair.com'}")
        print(new_line)

        
# Function that reads the product data file into a dictionary
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


# Function that reads the customer order data file into a list
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

# Function that exits to program
def end_program():
    exit()

# Call main to start this program. Check if program is being started or imported.
if __name__ == "__main__":
    main()


