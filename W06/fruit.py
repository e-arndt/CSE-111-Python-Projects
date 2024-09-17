# Author: Eric Arndt
# Class: CSE 111 W06 Object List - Fruit

# CREATIVITY: 

# Import OS module used to check which OS is in use
import os

# Set static variables
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "FRUIT LIST "
result_banner              = "*** "


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


def main():
        # Call function to clear terminal screen
        clrscr()


        # Call function to print banner
        welcome()


        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original list: {fruit_list}")


        # Reverse the order of the fruit list
        fruit_list.reverse()
        print(f"reverse list : {fruit_list}")


        # Append 'orange' to the list
        fruit_list.append("orange")
        print(f"append orange: {fruit_list}")


        # Find apple, insert cherry before apple
        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"insert cherry: {fruit_list}")


        # Find banana in list and remove it
        index = fruit_list.index("banana")
        fruit_list.pop(index)
        print(f"remove banana: {fruit_list}")


        # Remove last item from list, print item removed and fruit list
        removed = fruit_list[-1]
        print(f"removed item : {removed}")
        fruit_list.pop()
        print(f"fruit list   : {fruit_list}")


        # Sort the list
        fruit_list.sort()
        print(f"sort the list: {fruit_list}")


        # Clear the list
        fruit_list.clear()
        print(f"list cleared : {fruit_list}")

        # Print space for better readability
        print(new_line)


# Check if the program is being imported or executed as a script
if __name__ == "__main__":
    main()