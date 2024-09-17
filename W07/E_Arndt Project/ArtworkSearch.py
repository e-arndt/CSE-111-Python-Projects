# Author: Eric Arndt
# Class: CSE 111 Student Project - Artwork Search
# Access a MySQL database called v_art using MySQL Connector for Python.
# Allow a user to search for various works of art by artist or keyword(boat, flowers, girl...).
# Using queries to the database, display results to the user, including painting title, artist, period and year.
# Load an image of the painting in a default browser or photo app for display by entering the artwork ID #.


# CREATIVITY: 
# It's all creative! 
# Key features include connecting to a sql DB
# A fair amount of input error handling
# Some missing file handling

# 'pathlib' module allows the program to 'discover' the path to the picture files
# as long as the pictures are in their folders and the folders are in the same folder as this program
# the program should be able to discover where the pictures are regardless of the path.

# Unique screen displays and formatting to make the output look aligned, clean, easy to read and entertaining.



# Import modules
import mysql.connector
import time
import webbrowser
import os
from pathlib import Path
import sys

# Determine where(path) this program started
ROOT_DIR       = Path(__file__).parent



# Set static variables
new_line                = '\n' # creates a new line
esc                     = '\x1b' # 'ESC' character
red_bg                  = esc + '[41m' # Turns on RED background
normal                  = esc + '[0m' # Turns background to normal
start_banner            = "ARTWORK SEARCH KIOSK"
artist_banner           = "SEARCH BY ARTIST"
keyword_banner          = "SEARCH BY KEYWORD"
exit_banner             = "GOODBYE!!"
art_input               = ["A", "a"] # List for use in checking for a valid user input, input MUST be in the list
key_input               = ["K", "k"] # List for use in checking for a valid user input, input MUST be in the list
exit_input              = ["E", "e"] # List for use in checking for a valid user input, input MUST be in the list
artist_input            = ["C", "c", "D", "d", "G", "g", "M", "m", "P", "p", "R", "r", "S", "s", "V", "v"] # List for use in checking for a valid user input, input MUST be in the list
artist_dict             = {"C": 4, "D": 3, "G": 5, "M": 6, "P": 7, "R": 2, "S": 8, "V": 1} # Dictionary for use in assigning the proper Artist_ID # from the artist the user chose.
keyword_input           = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"] # List for use in checking for a valid user input, input MUST be in the list
artwork_ids             = [] # List for storing selected artwork ID #s
artwork_files           = [] # List for storing the filename of selected artwork




# Set function for clearing terminal screen
def clrscr():
    # Check if Operating System is Mac and Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')



# Function to display welcome or program main screen banner
def welcome():
    t = .1
    # Print "Welcome" Banner / box
    print(red_bg + start_banner.center(50,' ') + normal)
    time.sleep(t)
    print(f"{red_bg + ' '+ normal:<58}{red_bg +' '+ normal}")
    time.sleep(t)
    print(f"{red_bg + ' '+ normal:<14}{'Welcome to the CSE 111 Art Gallery Kiosk'}{red_bg + ' '+ normal:^18}")
    time.sleep(t)
    print(f"{red_bg + ' '+ normal:<13}{'Use the kiosk to search for information on'}{red_bg + ' '+ normal:^16}")
    time.sleep(t)
    print(f"{red_bg + ' '+ normal:<15}{'various works of art and their artists'}{red_bg + ' '+ normal:^20}")
    time.sleep(t)
    print(f"{red_bg + ' '+ normal:<14}{'Use the ID # to see a picture of the art'}{red_bg + ' '+ normal:^19}" )
    time.sleep(t)
    print(f"{red_bg + ' '+ normal:<58}{red_bg +' '+ normal}")
    time.sleep(t)
    print(f"{red_bg + ' ' * 49 + normal:<58}{red_bg +' '+ normal}")
    time.sleep(t)
    print()


# Function to display banner for the search by artist screen
def SBA_banner():
        # Print "search by artist" Banner
        print(red_bg + artist_banner.center(50,' ') + normal + new_line)


# Function to display banner for the search by keyword screen
def SBK_banner():
        # Print "search by keyword" Banner
        print(red_bg + keyword_banner.center(50,' ') + normal + new_line)
        


# Function to display banner when exiting the program
def gb_banner():
        # Print "Exit" Banner
        print(red_bg + exit_banner.center(50,' ') + normal + new_line)


# Function to login to DB, execute query and return results
def db_query(sql, key):
    artdb = mysql.connector.connect(
        host="localhost",
        user="python",
        password="",
        database="v_art"
)
    mycursor = artdb.cursor()

    mycursor.execute(sql, key)
    query_result = mycursor.fetchall()

    return query_result

# Function for searching by artist
def search_by_artist():
      
    # Set indexs for retrieving data
    fname_index     = 0
    mname_index     = 1
    lname_index     = 2
    dob_index       = 3
    dod_index       = 4
    country_index   = 5
    title_index     = 6
    art_year_index  = 7
    period_index    = 8
    art_desc_index  = 9
    art_type_index  = 10
    art_loc_index   = 11
    art_file_index  = 12
    art_id_index    = 13
    

    clrscr() # Clear terminal screen
    SBA_banner() # Display Search By Artist banner
    # Display artist options for user to choose
    print("Venture Coy         [C]")
    print("Leonardo da Vinci   [D]")
    print("Deborah Gill        [G]")
    print("Claude Monet        [M]")
    print("Pablo Picasso       [P]")
    print("Michelangelo Simoni [S]")
    print("Vincent van Gogh    [V]")
    print("Rembrandt van Rijn  [R]")
    print()

    # User input of artist
    user_artist = input("Choose the artist: ")

    # Check if user input is in the 'artist_input' list 
    if user_artist in artist_input:
        artist_id = artist_dict[user_artist.upper()]
        
        # Set SQL Query string for use in retrieving requested data
        sql = "SELECT fname, mname, lname, dob, dod, country, title, artyear, period, artdescription, arttype, artlocation, artfile, artwork_id  FROM artist JOIN artwork USING(artist_id) WHERE artist_id = %s"
        key = (artist_id, )

        # Send sql query to DB
        result = db_query(sql, key)
        
        # Read artist data into variables
        for each in result:
            fname    = each[fname_index]
            mname    = each[mname_index]
            lname    = each[lname_index]
            dob      = each[dob_index]
            dod      = each[dod_index]
            country  = each[country_index]
            
        # If the Date Of Death(dod) = None, assume the artist is still living and replace 'None' with 'Living'
        if dod == None:
             dod = "Living"

        # If Middle Name(mname) = None, then run this code to not use or print it
        if mname == None:

            # Set name variable to use first and last names only
            aname = (f"{fname} {lname}")

            # Clear screen and print result banner that includes the name of the artist selected
            clrscr()
            print()
            artist_name = (f"RESULTS FOR {aname.upper()}")
            print(red_bg + artist_name.center(50,' ') + normal + new_line)
           
            # Display artist info
            print(f"ARTIST : {fname} {lname}")
            print(f"BIRTH  : {dob}")
            print(f"DEATH  : {dod}")
            print(f"COUNTRY: {country}")
            print()
            
            # Read artwork data into variables
            for item in result:
                
                title      = item[title_index]
                art_year   = item[art_year_index]
                art_period = item[period_index]
                art_desc   = item[art_desc_index]
                art_type   = item[art_type_index]
                art_loc    = item[art_loc_index]
                art_file   = item[art_file_index]
                art_id     = item[art_id_index]
                
                # Display artwork info and save artwork ID and filename to lists
                print(f"ARTWORK NAME: {title}")
                print(f"YEAR CREATED: {art_year}")
                print(f"ART PERIOD  : {art_period}")
                print(f"DESCRIPTION : {art_desc}")
                print(f"ART MEDIUM  : {art_type}")
                print(f"ART LOCATION: {art_loc}")
                print(f"ARTWORK ID# : {art_id}")
                artwork_ids.append(art_id)
                artwork_files.append(art_file)
                print()

            # Call get_art_id function which asks the user which artwork they want to see
            art_id = get_art_id()
            # Take that input from the user and pass it to the show_artwork function for displaying the picture of that artwork
            show_artwork(art_id)

        # else the artist has a middle name, so run this code to use first middle and last names
        else:
            # But for the banner we will just use first and last names
            aname = (f"{fname} {lname}")

            # Clear screen and print result banner that includes the name of the artist selected
            clrscr()
            artist_name = (f"RESULTS FOR {aname.upper()}")
            print(red_bg + artist_name.center(50,' ') + normal + new_line)
           
            # Print artist info, including the middle name
            print(f"ARTIST : {fname} {mname} {lname}")
            print(f"BIRTH  : {dob}")
            print(f"DEATH  : {dod}")
            print(f"COUNTRY: {country}")
            print()
            
            # Read artwork data into variables
            for item in result:
                
                title      = item[title_index]
                art_year   = item[art_year_index]
                art_period = item[period_index]
                art_desc   = item[art_desc_index]
                art_type   = item[art_type_index]
                art_loc    = item[art_loc_index]
                art_file   = item[art_file_index]
                art_id     = item[art_id_index]
                
                # Display artwork info and save artwork ID and filename to lists
                print(f"ARTWORK NAME: {title}")
                print(f"YEAR CREATED: {art_year}")
                print(f"ART PERIOD  : {art_period}")
                print(f"DESCRIPTION : {art_desc}")
                print(f"ART MEDIUM  : {art_type}")
                print(f"ART LOCATION: {art_loc}")
                print(f"ARTWORK ID# : {art_id}")
                artwork_ids.append(art_id)
                artwork_files.append(art_file)
                print()

            # Call get_art_id function which asks the user which artwork they want to see
            art_id = get_art_id()
            # Take that input from the user and pass it to the show_artwork function for displaying the picture of that artwork
            show_artwork(art_id)
            
    # Else assume an invalid input was entered
    else:
        # Display what was entered, indicate that it was invalid
        print(f"{user_artist} is not a valid entry.")
        # Display for 3 seconds
        time.sleep(3)
        # Start the function again for a new input from user
        search_by_artist()


# Function for searching by keyword
def search_by_keyword():

    # Set indexs for retrieving data
    fname_index     = 0
    mname_index     = 1
    lname_index     = 2
    dob_index       = 3
    dod_index       = 4
    country_index   = 5
    title_index     = 6
    art_year_index  = 7
    period_index    = 8
    art_desc_index  = 9
    art_type_index  = 10
    art_loc_index   = 11
    art_file_index  = 12
    art_id_index    = 13
    art_keyword     = 14
    

    clrscr() # Clear terminal screen
    SBK_banner() # Display Search By Keyword banner
    # Display keyword options for user to choose
    print("Main Menu [0]")
    print("Flowers   [1]")
    print("Blue      [2]")
    print("Landscape [3]")
    print("Girl      [4]")
    print("People    [5]")
    print("Battle    [6]")
    print("Boat      [7]")
    print("Water     [8]")
    print("Christ    [9]")
    print("Food      [10]")
    print("Baby      [11]")
    print()

    # User input of keyword
    user_key = input("Choose a keyword: ")
    
    # Check if the user entered zero(0), if so go to the main() function / screen
    if user_key == "0":
        main()
    
    # Check if user input is in the 'keyword_input' list
    if user_key in keyword_input:

        # Set SQL Query string for use in retrieving requested data
        sql = "SELECT fname, mname, lname, dob, dod, country, title, artyear, period, artdescription, arttype, artlocation, artfile, artwork_id, keyword FROM artist JOIN artwork USING(artist_id) JOIN artwork_keyword USING(artwork_id) JOIN keyword USING(keyword_id) WHERE keyword_id = %s"
        key = (user_key, )

        # Send sql query to DB
        result = db_query(sql, key)
        
        # Read artist data into variables
        for each in result:
            fname    = each[fname_index]
            mname    = each[mname_index]
            lname    = each[lname_index]
            dob      = each[dob_index]
            dod      = each[dod_index]
            country  = each[country_index]
            keyword  = each[art_keyword]
            
        # If the Date Of Death(dod) = None, assume the artist is still living and replace 'None' with 'Living'
        if dod == None:
             dod = "Living"

        # If Middle Name(mname) = None, then run this code to not use or print it
        if mname == None:

            # Clear screen and print result banner that includes the keyword selected
            clrscr()
            keyword_name = (f"RESULTS FOR KEYWORD '{keyword.upper()}'")
            print(red_bg + keyword_name.center(50,' ') + normal + new_line)
           
            # Read artwork data into variables
            for item in result:
                
                fname      = item[fname_index]
                lname      = item[lname_index]
                title      = item[title_index]
                art_year   = item[art_year_index]
                art_period = item[period_index]
                art_desc   = item[art_desc_index]
                art_type   = item[art_type_index]
                art_loc    = item[art_loc_index]
                art_file   = item[art_file_index]
                art_id     = item[art_id_index]
                
                # Display artwork info and save artwork ID and filename to lists
                print(f"ARTIST : {fname} {lname}")
                print(f"ARTWORK NAME: {title}")
                print(f"YEAR CREATED: {art_year}")
                print(f"ART PERIOD  : {art_period}")
                print(f"DESCRIPTION : {art_desc}")
                print(f"ART MEDIUM  : {art_type}")
                print(f"ART LOCATION: {art_loc}")
                print(f"ARTWORK ID# : {art_id}")
                artwork_ids.append(art_id)
                artwork_files.append(art_file)
                print()

            # Call get_art_id function which asks the user which artwork they want to see
            art_id = get_art_id()
            

        # else the artist has a middle name, so run this code to use first middle and last names
        else:
            
            # Clear screen and print result banner that includes the keyword selected
            clrscr()
            keyword_name = (f"RESULTS FOR KEYWORD '{keyword.upper()}'")
            print(red_bg + keyword_name.center(50,' ') + normal + new_line)
           
            # Read artwork data into variables
            for item in result:
                
                fname      = item[fname_index]
                mname      = item[mname_index]
                lname      = item[lname_index]
                title      = item[title_index]
                art_year   = item[art_year_index]
                art_period = item[period_index]
                art_desc   = item[art_desc_index]
                art_type   = item[art_type_index]
                art_loc    = item[art_loc_index]
                art_file   = item[art_file_index]
                art_id     = item[art_id_index]
                
                # Display artwork info and save artwork ID and filename to lists
                print(f"ARTIST : {fname} {mname} {lname}")
                print(f"ARTWORK NAME: {title}")
                print(f"YEAR CREATED: {art_year}")
                print(f"ART PERIOD  : {art_period}")
                print(f"DESCRIPTION : {art_desc}")
                print(f"ART MEDIUM  : {art_type}")
                print(f"ART LOCATION: {art_loc}")
                print(f"ARTWORK ID# : {art_id}")
                artwork_ids.append(art_id)
                artwork_files.append(art_file)
                print()

            # Call get_art_id function which asks the user which artwork they want to see
            art_id = get_art_id()
            
    # Else assume an invalid input was entered    
    else:
        # Display what was entered, indicate that it was invalid
        print(f"{user_key} is not a valid entry.")
        # Display for 3 seconds
        time.sleep(3)
        # Start the function again for a new input from user
        search_by_keyword()


# Function that requests the user to select the ID # of the artwork they wish to see
def get_art_id():
    
    # Gets input from the user of the artwork they wish to view
    art_id = (input("Enter Artwork ID# or Zero(0) for Main Menu: "))

    # Checks the input to see if it is a letter
    if art_id.isalpha():
        # if input is a letter a meesage is displayed requesting that a number be entered
        print("A number must be entered, try again.")
        # Display for 2 seconds
        time.sleep(2)
        # Back-up and erase two lines of text
        for loop in range(2):
            sys.stdout.write("\033[F") #back to previous line 
            sys.stdout.write("\033[K") #clear line
        # Recall the get_art_id function so user can try again
        get_art_id()

    # else the input must be a number, change the input to an integer
    else:
        art_id = int(art_id)

    # If the integer number is in the artwork_ids list then call the show_artwork function
    if art_id in artwork_ids:
        show_artwork(art_id)
        
    # If the the number is not in the list, see if it is a zero(0), if it is call the main function
    elif art_id == 0:
        main()

    # else if none of these match then the input is not valid
    else:
        # Print message that the input is not valid
        print(f"{art_id} is not valid, valid entries are {artwork_ids}")
        # Display for 4 seconds
        time.sleep(4)
        # Back-up and erase two lines of text
        for loop in range(2):
            sys.stdout.write("\033[F") #back to previous line 
            sys.stdout.write("\033[K") #clear line 
        
        # Restart get_art_id function
        get_art_id()

    # Restart get_art_id function
    get_art_id()


# Function to display the selected(art_id) artwork
def show_artwork(art_id):

    # Set SQL Query string for use in retrieving data need to display the requested picture
    sql = "SELECT artfile, lname, fname FROM artwork JOIN artist USING(artist_id) WHERE artwork_id = %s"
    key = (art_id, )

    # Send sql query to the DB and retrieve the required data
    artfile = db_query(sql, key)
    
    # Read filename and path data into variables
    for file in artfile:
        filename = file[0]
        folder   = file[1]
        first    = file[2]

    # Read order request file / Error handling for missing file
    try:
        # From ROOT_DIR(where this program was started) add the name of the folder(artist last name) where the pictures are
        folder_path = ROOT_DIR / folder
        # From the ROOT_DIR/folder path add the name of the picture filename to create the complete 'file_path'
        file_path   = folder_path / filename

    # in case of TypeError due to missing path / file, do the following
    except TypeError:
        print(f"ERROR: {filename} not found!!")
        print(f"Expected {filename} at {file_path}", file=sys.stderr)
        print(new_line) 
    

    # Error handling for missing file due to FileNotFoundError
    except FileNotFoundError:
        print(f"ERROR: Path or File not found!!")
        print(f"Expected file at {file_path}", file=sys.stderr)
        print(new_line) 
        

    #Error handling for file permission errors
    except PermissionError:
        print(f"ERROR: Insufficient permission to read file")
        print(f"at {file_path}", file=sys.stderr)
        print(new_line) 
        
    # Once the data is retrieved from the DB, display the following info about the picture file and path
    print()
    print(f"ART ID#  : {art_id}")
    print(f"FILE PATH: {folder_path}")
    print(f"FILE NAME: {filename}")
    print(f"ARTIST   : {first} {folder}")
    print()
    
    # Read order request file / Error handling for missing file
    try:
        # Open a web browser or default photo app to display a picture of the art requested
        # using the constructed file path and filename
        webbrowser.open_new_tab(file_path)

    # in case of TypeError due to missing path / file, do the following
    except TypeError:
        print(f"ERROR: {filename} not found!!")
        print(f"Expected {filename} at {file_path}", file=sys.stderr)
        
    
    # Error handling for missing file due to FileNotFoundError
    except FileNotFoundError:
        print(f"ERROR: {filename} not found!!")
        print(f"Expected {filename} at {file_path}", file=sys.stderr)
         

    #Error handling for file permission errors
    except PermissionError:
        print(f"ERROR: Insufficient permission to read 'request.csv' file")
        print(f"at {file_path}", file=sys.stderr)
        
    # After the file data and picture are displayed, wait for a user input to contiune 
    input("Press Enter Key ")
    # Back-up and erase 8 lines of text so user can choose another picture
    for loop in range(8):
        sys.stdout.write("\033[F") #back to previous line 
        sys.stdout.write("\033[K") #clear line 
    
    # Return to get_art_id function and ask user to input another art ID to display or go to the main menu main() function
    return

# main function
def main():
    # clear the terminal screen
    clrscr()
    # Print the main menu / welcome screen
    welcome()
    # Wait for a 'hair' over 1/3 of a second (purely for effect)
    time.sleep(.35)
    # Ask user to choose to search by Artist, by Keyword or to exit the program
    user_search_type = input("  Search by Artist, Keyword or Exit [A, K, E]: ")
    
    # If the user input matches an option in the art_input list, then call the search_by_artist function
    if user_search_type in art_input:
        search_by_artist()

    # If the user input matches an option in the key_input list, then call the search_by_keyword function
    elif user_search_type in key_input:
        search_by_keyword()

    # If the user input matches an option in the exit_input list, then execute the following
    elif user_search_type in exit_input:
        # Clear terminal screen
        clrscr()
        # Display the goodbye / exit banner
        gb_banner()
        # Print a space / new line
        print(new_line)
        # Call the end_program function
        end_program()
    
    # Any other input is considered not valid
    else:
        print(f"{user_search_type} is not a valid entry.")
        time.sleep(3)
        main()

    # Restart the main function
    main()



# Function that exits to program
def end_program():
    time.sleep(2)
    clrscr()
    exit()
    

# Call main to start this program. Check if program is being started or imported.
if __name__ == "__main__":
    main()
