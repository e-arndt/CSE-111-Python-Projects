# Creativity:
# User can "ADD" items, prices and quantities to a shopping cart.
# Contents of the shopping cart can be displayed.
# Items can be removed from the shopping cart.
# Added a subtotal function for shopping cart, items can be calculated and displayed.
# Added a purchase / checkout function which checks the subtotal and day of the week for possible discount.
# Created individual screens for each menu function.
# Added a banner to top of each screen to identify the current function.
# Gave user the ability to update the quantity of items already in the cart.
# Aligned Item, Price and Quantity for improved formatting.
# Check if cart is empty then display "Cart is empty" to user rather than just a blank screen.
# Some error handling added to ensure that some inputs are within proper range or
# alpha characters are rejected when expecting only numbers.

# Author: Eric Arndt
# Class: CSE 111 W01 Shopping Cart with auto discount of 10% on Tue and Wed


# Import libraries and set variables
import os
import time
import datetime
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
main_banner         = "SHOPPING CART MENU"
add_banner          = "ADD ITEM / UPDATE"
cart_banner         = "SHOPPING CART ITEMS"
remove_banner       = "SHOPPING CART ITEM REMOVAL"
total_banner        = "SHOPPING CART TOTAL"
checkout_banner     = "CHECKOUT / PURCHASE TOTAL"
new_line            = "\n"
new_item            = ""
new_price           = 0
cart                = 0
discount            = 0
discount_rate       = .10
sub_total           = 0
tax_rate            = 0.06
tax                 = 0
total               = 0
remove_num          = 0
cart_total          = 0
cart_subtotal       = 0
quantity            = 0
today               = 0
day_of_week         = 0
list_items          = []
list_prices         = []
list_quantity       = []
run                 = "Y"


# Main while loop, runs until user quits
while run == "Y" or run == "y":
    
# Set function for clearing terminal screen
    def clrscr():
    # Check if Operating System is Mac and Linux
        if os.name == 'posix':
            _ = os.system('clear')
        else:
    # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')

# Set function for displaying the main menu
    def menu():
        clrscr()
        print(red_bd + main_banner.center(50,' ') + normal + new_line)
        print("1. Add a new item / Update quantity")
        print("2. Display shopping cart")
        print("3. Remove an item from cart")
        print("4. Compute cart total")
        print("5. Purchase items in cart")
        print("6. Quit")
        print(new_line)
        
# Call menu function and request user to select a menu option
    menu()
    cart = 0
    today = datetime.datetime.today()
    menu_opt = (input("Select an option: "))
    # Check user input to ensure a number was entered, if not, ask user to try again
    if menu_opt.isalpha():
        print("A number must be entered, try again.")
        time.sleep(2)
        menu()
    else:
        menu_opt = int(menu_opt)
        # If option 1 selected, perform Add Item / Quantity 
        if menu_opt == 1:
            clrscr()
            print(red_bd + add_banner.center(50,' ') + normal + new_line)
            # Read Item, Price and Quantity lists
            for num in range(len(list_items)):
                    item  = (list_items[num])
                    price = (f"${list_prices[num]:.2f}")
                    quan  = (list_quantity[num])
                    item_num = num + 1
                    item_num = (f"{item_num}.")
                    # Print Item, Price and Quantity lists to user
                    print(f"{item:<13} {price:^7} Qty {quan}")
            print(new_line)
            # Request input from user for new item or cart item to update
            new_item = input("Name of item to add / update: ")
            for index in range(len(list_items)):
                items = list_items[index]
                # If user input is already in the list
                if new_item.lower() == items.lower():
                    print(new_line)
                    # Request new quantity from user
                    amt_change = input(f"Change {list_items[index]} from {list_quantity[index]} to: ")
                    # If input is 0 or less, tell user to use option 3 to remove items from cart
                    if int(amt_change) <= 0:
                        print("Zero(0) quantity not vaild, Please use Option 3 to remove items.")
                        time.sleep(3)
                        cart = 1
                        menu()
                    # Otherwise update the quantity in the list with the new quantity input from user
                    else:
                        list_quantity[index] = amt_change
                        print(f"'{list_items[index]}' has been changed to {list_quantity[index]}.")
                        time.sleep(2)
                        cart = 1
                        menu()
            # If the item is not already in the list, continue with inputting the new item's price and quantity
            if cart == 0:
                # Add the name of the new item to the item list
                list_items.append(new_item)
                # Request price input from user
                new_price     = float(input("Item price: $"))
                # Add new item's price to the price list
                list_prices.append(new_price)
                quantity      = input("Item quantity: ")
                amount = int(quantity)
                # if user inputs a quantity of 0 or less, reject the input
                if amount <= 0:
                    print(f"'{quantity}' is an invalid quantity.")
                    time.sleep(2)
                    menu()
                # Otherwise add the new item's quantity to the list
                else:
                    list_quantity.append(quantity)
                    print(f"'{new_item}' has been added.")
                    time.sleep(1)
                    menu()

        # If option 2 selected, display current contents of cart to the user
        elif menu_opt == 2:
            clrscr()
            print(red_bd + cart_banner.center(50,' ') + normal + new_line)
            # If item list is empty, tell user the cart is currently empty
            if (len(list_items) == 0):
                print("Cart is empty")
            # Otherwise recall item names from item list and print contents to user
            else:
                for num in range(len(list_items)):
                    item  = (list_items[num])
                    price = (f"${list_prices[num]:.2f}")
                    quan  = (list_quantity[num])
                    item_num = num + 1
                    item_num = (f"{item_num}.")
                    # Display Item number, Item name, Price and Quantity to user
                    print(f"{item_num:<2} {item:<13} {price:^7} Qty {quan}")
            print(new_line)
            back = input("Press enter for main menu.")
            menu()
        # If option 3 selected, display current cart contents and prompt user for the number of the item to be removed
        elif menu_opt == 3:
            clrscr()
            print(red_bd + remove_banner.center(50,' ') + normal + new_line)
            # Read current item names, prices and quantity from lists
            for num in range(len(list_items)):
                    item  = (list_items[num])
                    price = (f"${list_prices[num]:.2f}")
                    qty   = (f"Qty {list_quantity[num]}")
                    item_num = num + 1
                    item_num = (f"{item_num}.")
                    # Display Item number, Item name, Price and Quantity to user
                    print(f"{item_num:<2} {item:<13} {price:^7} {qty}")
            print(new_line)
            item_len = (len(list_items))
            # while loop to deal with possible Error if a number is not entered
            while True:
                try:
                    # Ask user to enter number of item to be removed from the cart
                    remove_num = int(input("Number of item to remove "))
                    break
                except ValueError:
                    # If user enters an invalid entry, they are notified and asked to try again
                    print("Invalid input.")
            # change user input to correctly align with list that starts with 0
            remove_item = (remove_num - 1)
            # Check if user input is "out of bounds" or too low / too high
            if remove_item < 0 or remove_num > item_len:
                print(f"Not a valid item number.")
                time.sleep(2)
            # Otherwise remove or "pop" the item, it's price and quantity from all 3 lists
            else:
                if int(list_quantity[remove_item]) >= 1:
                    print(f"'{list_items[remove_item]}' has been removed.")
                    list_items.pop(remove_item)
                    list_prices.pop(remove_item)
                    list_quantity.pop(remove_item)
                    time.sleep(2)
                    menu()
                
        # If option 4 is selected, display the total value of the cart's items
        elif menu_opt == 4:
            clrscr()
            print(red_bd + total_banner.center(50,' ') + normal + new_line)
            # Read current item names, prices and quantity from lists
            for num in range(len(list_items)):
                    item  = (list_items[num])
                    price = (f"${list_prices[num]:.2f}")
                    qty   = (f"Qty {list_quantity[num]}")
                    item_num = num + 1
                    item_num = (f"{item_num}.")
                    # Display Item number, Item name, Price and Quantity to user
                    print(f"{item_num:<2} {item:<13} {price:^7} {qty}")
            print(new_line)
            # Loop through the entire item list
            for num in range(len(list_prices)):
                # Read each item from all 3 lists as the loop progresses from item to item in the lists
                # Calculate a total buy taking the price of each item and multiplying it by the associated quantity
                cart_total = cart_total + float(list_prices[num]) * float(list_quantity[num])
                # Display that total to the user
            print(f"Total price of shopping cart items: ${cart_total:.2f}")
            print(new_line)
            back = input("Press enter for main menu.")
            cart_total = 0
            menu()
        # If option 5 is selected, calculate cart subtotal, discounts and taxes
        # Check for applicable discounts based of day of week(Tuesday or Wednesday) and if $50+ subtotal
        # Display new subtotal and total for checkout
        elif menu_opt == 5:
            clrscr()
            print(red_bd + checkout_banner.center(50,' ') + normal + new_line)
            # Read current item names, prices and quantity from lists
            for num in range(len(list_items)):
                    item  = (list_items[num])
                    price = (f"${list_prices[num]:.2f}")
                    qty   = (f"Qty {list_quantity[num]}")
                    item_num = num + 1
                    item_num = (f"{item_num}.")
                    cart_subtotal = cart_subtotal + float(list_prices[num]) * float(list_quantity[num])
                    # Display Item number, Item name, Price and Quantity to user
                    print(f"{item_num:<2} {item:<13} {price:^7} {qty}")
            print()
            # Loop through the entire item list
            for num in range(len(list_prices)):
                # Read each item from all 3 lists as the loop progresses from item to item in the lists
                # Calculate a total buy taking the price of each item and multiplying it by the associated quantity
                # Check if day of the week is Tue or Wed and if cart subtotal is $50 or more, if so, apply 10% discount
                if (today.weekday() == 1 or today.weekday() == 2) and cart_subtotal >= 50:
                    cart_total = cart_total + float(list_prices[num]) * float(list_quantity[num])
                    discount = (cart_total * discount_rate)
                    sub_total = cart_total - discount
                    tax = (sub_total * tax_rate)
                    total = (sub_total + tax)
                else:
                    # If day of week or subtotal doesn't qualify for discount, execute this code instead (no discount)
                    cart_total = cart_total + float(list_prices[num]) * float(list_quantity[num])
                    sub_total = cart_total
                    tax = (sub_total * tax_rate)
                    total = (sub_total + tax)
                # Display any discounts and totals to the user
            print(f"Subtotal BEFORE Discount: ${cart_total:.2f}")
            print(f"Applied {discount_rate * 100}% Discount  :  ${discount:.2f}")
            print(f"Subtotal AFTER Discount : ${sub_total:.2f}")
            print(f"Local Sales Tax at 6%   :  ${tax:.2f}")
            print("----------------------------------")
            print(f"Total Purchase Price    : ${total:.2f}")
            print(new_line)
            # Reset variables to 0 for new purchases
            cart_total = 0
            cart_subtotal = 0
            discount = 0
            sub_total = 0
            tax = 0
            total = 0
            back = input("Press P to purchase items or any other key for menu.")
            if back == "P" or back == "p":
                # Reset variables to 0 for new purchases
                cart_total = 0
                cart_subtotal = 0
                discount = 0
                sub_total = 0
                tax = 0
                total = 0
                list_items    = []
                list_prices   = []
                list_quantity = []
                print("Thank you for your purchase.")
                time.sleep(3)
                menu()
            else:
                # Reset variables to 0 for new purchases
                cart_total = 0
                cart_subtotal = 0
                discount = 0
                sub_total = 0
                tax = 0
                total = 0
                menu()
        # If option 6, set run to "N" so the main while loop will exit the program
        elif menu_opt == 6:
            print(new_line)
            run = "N"
        # If the loop drops to this point, a valid option was not selected, tell the user and start again
        else:
            print("Please enter a valid number")
            time.sleep(2)
            run = "Y"

    
# Main while loop, "Y" to continue running, "N" to exit the program
if (run == "Y" or run == "y"):
    clrscr()
elif (run != "Y" or run != "y"):
    print("Bye...")
    print(new_line)
    time.sleep(2)
    clrscr()
