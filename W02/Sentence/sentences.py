# Author: Eric Arndt
# Class: CSE 111 W03 Sentence Constructor
# Construct a sentence with a determiner, a noun and a verb
# Display constructed sentence to user.

# Import modules
import os
import random


# Set the variable "path" to the drive and folder location of the data file
single_determiner_path     = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\BYUi\\CSE 111 Prep\\Single-Determiners.txt"
single_noun_path           = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\BYUi\\CSE 111 Prep\\Single-Nouns.txt"
single_present_verb_path   = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\BYUi\\CSE 111 Prep\\Single-Present-Verbs.txt"

plural_determiner_path     = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\BYUi\\CSE 111 Prep\\Plural-Determiners.txt"
plural_noun_path           = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\BYUi\\CSE 111 Prep\\Plural-Nouns.txt"
plural_present_verb_path   = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\BYUi\\CSE 111 Prep\\Plural-Present-Verbs.txt"

past_verb_path             = "D:\\Users\\Eric\\Documents\\Education\\BYU_Pathways\\BYUi\\CSE 111 Prep\\Past-Verbs.txt"



# Set static variables
new_line                   = '\n'
esc                        = '\x1b'
normal                     = esc + '[0m'
red_bg                     = esc + '[41m' 
welcome_banner             = "SENTENCE CONSTRUCTOR "
result_banner              = "YOUR NEW SENTENCE "
text                       = 'Test'
run                        = "Y"
tense                      = ""
single_count               = 0
plural_count               = 0
tense_count                = 0
quantity                   = 0
single_determiner_list     = []
plural_determiner_list     = []
single_noun_word_list      = []
plural_noun_word_list      = []
single_present_verb_list   = []
plural_present_verb_list   = []
past_verb_list             = []
choose_tense               = ["past", "present", "future"]


while run == "Y" or run == "y":
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


      # Set main function
    def main():
        # Read word files
        read_determiner_file()
        read_noun_file()
        read_verb_file()
        
        sentence = make_sentence()
        print (sentence)
            
            

    def tense_selector():
            tense = random.choice(choose_tense)
            #print(f"Tense Sel: {tense}")
            
            return tense 


    def sp_selector():
        quantity = random.randint(0,1)      
        #print(f"Qty Sel : {quantity}")
           
        return quantity


    def make_sentence():
        determiner_word = get_determiner()
        noun_word       = get_noun()
        verb_word       = get_verb()

        sentence = (f"{determiner_word} {noun_word} {verb_word}.")
            
        return sentence


    def get_determiner():
        qty = sp_selector()
        #print(f"Get Deter: {qty}")
        if qty == 1:
                words = single_determiner_list
        else:
                words = plural_determiner_list

        word = random.choice(words)
        determiner_word = word.capitalize()

        return determiner_word


    def get_noun():
        qty = sp_selector()
        #print(f"Get Noun : {qty}")
        if qty == 1:
                words = single_noun_word_list
        else:
                words = plural_noun_word_list

        noun_word = random.choice(words)

        return noun_word


    def get_verb():
        qty = sp_selector()
        tense = tense_selector()
        #print(f"Get Verb: {tense} {qty}")
        if   tense == "past":
                words = past_verb_list
                verb_word = random.choice(words)
        elif tense == "future":
                words = single_present_verb_list
                word  = random.choice(words)
                verb_word = (f"will {word}")
        elif tense == "present" and qty == 1:
                words = single_present_verb_list
                verb_word = random.choice(words)
        else:
                words = plural_present_verb_list
                verb_word = random.choice(words)

        return verb_word



    def read_determiner_file():
        with open(single_determiner_path, "r") as determiner_data:

                # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                header = next(determiner_data)

                # Loop to step through each line of data in the file
                for determiner in determiner_data:
                    # Strip off whitespaces in data string
                    determiner_record = determiner.strip()
                    # Split string of data into separate parts by looking for a ","
                    determiner_record = determiner.split(",")
                    #determiner_record = determiner.lower()
                    determiner_word   = determiner_record[0]
                        
                    single_determiner_list.append(determiner_word)



        with open(plural_determiner_path, "r") as determiner_data:

                # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                header = next(determiner_data)

                # Loop to step through each line of data in the file
                for determiner in determiner_data:
                    # Strip off whitespaces in data string
                    determiner_record = determiner.strip()
                    # Split string of data into separate parts by looking for a ","
                    determiner_record = determiner.split(",")
                    #determiner_record = determiner.lower()
                    determiner_word   = determiner_record[0]
                        
                    plural_determiner_list.append(determiner_word)
                  


    def read_noun_file():
        with open(single_noun_path, "r") as noun_data:

                # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                header = next(noun_data)

                # Loop to step through each line of data in the file
                for noun in noun_data:
                    # Strip off whitespaces in data string
                    noun_record = noun.strip()
                    # Split string of data into separate parts by looking for a ","
                    noun_record = noun.split(",")
                    noun_word   = noun_record[0]
                  
                    single_noun_word_list.append(noun_word)



        with open(plural_noun_path, "r") as noun_data:

                # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                header = next(noun_data)

                # Loop to step through each line of data in the file
                for noun in noun_data:
                    # Strip off whitespaces in data string
                    noun_record = noun.strip()
                    # Split string of data into separate parts by looking for a ","
                    noun_record = noun.split(",")
                    noun_word   = noun_record[0]
                        
                    plural_noun_word_list.append(noun_word)



    def read_verb_file():
        with open(single_present_verb_path, "r") as verb_data:

                # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                header = next(verb_data)

                # Loop to step through each line of data in the file
                for verb in verb_data:
                    # Strip off whitespaces in data string
                    verb_record = verb.strip()
                    # Split string of data into separate parts by looking for a ","
                    verb_record = verb.split(",")
                    verb_word   = verb_record[0]
                    verb_word   = verb_word.lower()
                        
                    single_present_verb_list.append(verb_word)



        with open(plural_present_verb_path, "r") as verb_data:

                # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                header = next(verb_data)

                # Loop to step through each line of data in the file
                for verb in verb_data:
                    # Strip off whitespaces in data string
                    verb_record = verb.strip()
                    # Split string of data into separate parts by looking for a ","
                    verb_record = verb.split(",")
                    verb_word   = verb_record[0]
                    verb_word   = verb_word.lower()
                        
                    plural_present_verb_list.append(verb_word)



        with open(past_verb_path, "r") as verb_data:

                # Read the first line of data from the file and store in the variable "header" then move to the next line of data
                header = next(verb_data)

                # Loop to step through each line of data in the file
                for verb in verb_data:
                    # Strip off whitespaces in data string
                    verb_record = verb.strip()
                    # Split string of data into separate parts by looking for a ","
                    verb_record = verb.split(",")
                    verb_word   = verb_record[0]
                    verb_word   = verb_word.lower()
                        
                    past_verb_list.append(verb_word)

      
      
                  


    # Call Clear Screen function
    clrscr()
    welcome()
    for i in range(6):
        main()
    print()
    run = (input('Run Again? [Y/N]: '))
    if (run == "Y" or run == "y"):
        clrscr()
        main()

    elif (run != "Y" or run != "y"):
        clrscr()
        run = "N"
      
#tense = random.choice(choose_tense)
#quantity = random.randint(0,1)
      

      