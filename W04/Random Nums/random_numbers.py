import os
import random

# Set static variables
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "RANDOM NUMBERS "
result_banner              = "RESULTS "



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


def append_random_numbers(numbers_list= [16.2, 75.1, 52.3], quantity=1):
    for amount in range(quantity):
            
            new_random_number = random.uniform(1, 100)
            round_random_number = round(new_random_number, 1)
            numbers_list.append(round_random_number)


def main():
    clrscr()
    welcome()
    numbers = [16.2, 75.1, 52.3]
    print(f"Original number list:  {numbers}")
    append_random_numbers(numbers)
    print(f"Add 1 number to list:  {numbers}")
    append_random_numbers(numbers, 3)
    print(f"Add 3 numbers to list: {numbers}")
    print(new_line)









if __name__ == "__main__":
    main()