# Author: Eric Arndt
# Class: CSE 111 W03 Sentence Constructor Milestone
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
single_determiner_list     = ["a", "one", "the"]
plural_determiner_list     = ["some", "many", "the"]
single_noun_word_list      = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
plural_noun_word_list      = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
single_present_verb_list   = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
plural_present_verb_list   = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
past_verb_list             = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
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

      # Set main function
      def main():

            # Print "Welcome" Banner
            print(red_bg + welcome_banner.center(50,' ') + normal + new_line)
            # Read word files
            #read_determiner_file()
            #read_noun_file()
            #read_verb_file()
            for i in range(6):
                sentence = make_sentence()
                print (sentence)
            
            
      


            

            



      def selector(quantity):
            tense = random.choice(choose_tense)
            #print(f"Tense: {tense}")
            quantity = random.randint(0,1)      
            #print(f"Qty  : {quantity}")
           
            

            return tense, quantity


      def make_sentence():
            determiner_word = get_determiner(quantity)
            noun_word       = get_noun(quantity)
            verb_word       = get_verb(quantity, tense)

            sentence = (f"{determiner_word} {noun_word} {verb_word}.")
            
            return sentence

      def get_determiner(quantity):
            """Return a randomly chosen determiner. A determiner is
            a word like "the", "a", "one", "some", "many".
            If quantity is 1, this function will return either "a",
            "one", or "the". Otherwise this function will return
            either "some", "many", or "the".
            Parameter
                quantity: an integer.
                    If quantity is 1, this function will return a
                    determiner for a single noun. Otherwise this
                    function will return a determiner for a plural
                    noun.
            Return: a randomly chosen determiner.
            """
            qty = selector(quantity)
            #quantity = random.randint(0,1)
            #print(f"Deter: {qty}")
            if qty == 1:
                  words = single_determiner_list
            else:
                  words = plural_determiner_list

            word = random.choice(words)
            determiner_word = word.capitalize()

            return determiner_word


      def get_noun(quantity):
            """Return a randomly chosen noun.
            If quantity is 1, this function will
            return one of these ten single nouns:
                "bird", "boy", "car", "cat", "child",
                "dog", "girl", "man", "rabbit", "woman"
            Otherwise, this function will return one of
            these ten plural nouns:
                "birds", "boys", "cars", "cats", "children",
                "dogs", "girls", "men", "rabbits", "women"
            Parameter
                quantity: an integer that determines if
                    the returned noun is single or plural.
            Return: a randomly chosen noun.
            """
            qty = selector(quantity)
            #quantity = random.randint(0,1)
            #print(f"Noun : {qty}")
            if qty == 1:
                  words = single_noun_word_list
            else:
                  words = plural_noun_word_list

            noun_word = random.choice(words)

            return noun_word


      def get_verb(quantity, tense):
            """Return a randomly chosen verb. If tense is "past",
            this function will return one of these ten verbs:
                "drank", "ate", "grew", "laughed", "thought",
                "ran", "slept", "talked", "walked", "wrote"
            If tense is "present" and quantity is 1, this
            function will return one of these ten verbs:
                "drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"
            If tense is "present" and quantity is NOT 1,
            this function will return one of these ten verbs:
                "drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"
            If tense is "future", this function will return one of
            these ten verbs:
                "will drink", "will eat", "will grow", "will laugh",
                "will think", "will run", "will sleep", "will talk",
                "will walk", "will write"
            Parameters
            quantity: an integer that determines if the
                returned verb is single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
            Return: a randomly chosen verb.
            """
            tense_qty = selector(quantity)
            #print(f"VERB: {tense_qty}")
            #v_tense = selector(tense)
            #print(f"VERB: {tense}")
            #quantity = random.randint(0,1)
            #tense = random.choice(choose_tense)
            #print(f"Verb: {v_tense} {tense_qty}")
            if   "past" in tense_qty:
                  #print("verb past")
                  words = past_verb_list
                  verb_word = random.choice(words)
            elif "future" in tense_qty:
                  #print("verb future")
                  words = single_present_verb_list
                  word  = random.choice(words)
                  verb_word = (f"will {word}")
            elif "present" in tense_qty and 1 in tense_qty:
                  #print("verb present 1")
                  words = single_present_verb_list
                  verb_word = random.choice(words)
            else:
                  #print("verb else")
                  words = single_present_verb_list
                  verb_word = random.choice(words)

            return verb_word


        # Used to expand vocabulary
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
                  

        # Used to expand vocabulary
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


        # Used to expand vocabulary
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
      # Call start or main function
      main()
      print()
      # Ask if user wants to run the program again
      run = (input('Run Again? [Y/N]: '))
      if (run == "Y" or run == "y"):
            clrscr()
            main()

      elif (run != "Y" or run != "y"):
            clrscr()
            run = "N"
      
      

      