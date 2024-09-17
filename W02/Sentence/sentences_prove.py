# Author: Eric Arndt
# Class: CSE 111 W02 Sentence Constructor Prove + Exceed requirements
# Construct a sentence with a determiner, a noun, a verb and a prepositional phrase
# Display constructed sentence to user.

# EXCEED REQUIREMENTS: Add an adjective to the sentences returned to the user.

# CREATIVE: Add a Welcome Banner that indicates the purpose of the program. Add clearing the Terminal Window,
# ask the user if they would like to run the program again or quit. Minor formatting for easier reading.

# Import modules, OS for clrearing the terminal window and RANDOM for the random choice generator
import os
import random



# Set static variables and lists
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
preposition_list           = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on","onto", "out", "over", "past", "to", "under", "with", "without"]
adjective_list             = ["abundant", "acceptable", "accurate", "adorable", "beige", "bronze", "blue", "brave", "bright", "brown", "black", "calm", "colorful", "copper", "cyan", "creative", "delicious", "eager", "elegant", "famous", "fragrant", "generous", "gold", "grey", "green","glorious", "graceful", "happy", "healthy", "honest", "humorous", "innocent", "joyful", "kind", "magnificent", "magenta", "mysterious", "naughty","neat", "nice", "obedient", "orange", "pink", "purple", "polite", "powerful", "quiet", "responsible", "radiant", "red", "ruby", "rich", "serious","silver", "scarlet", "smart", "strong", "talented", "tan", "turquoise", "tender", "trustworthy", "unique", "useful", "vast", "violet", "white", "wise", "yellow"]

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
           
            for i in range(6):
                sentence = make_sentence()
                print (sentence)
            

    # Randomly select tense and quantity (singular, plural)
    def selector(quantity):
            tense = random.choice(choose_tense)
            
            quantity = random.randint(0,1)      
            
           
            

            return tense, quantity


    def make_sentence():
            """Return a constructed sentence
            made from a determiner word, an adjective, a noun, a verb and a prepositional phrase.
            The propositional phrase consists of prepositional word, a determiner word and a noun.
            """
            determiner_word = get_determiner(quantity)
            adjective_word  = get_adjective()
            noun_word       = get_noun(quantity)
            verb_word       = get_verb(quantity, tense)
            prep_phrase     = get_prepositional_phrase(quantity)

            sentence = (f"{determiner_word.capitalize()} {adjective_word} {noun_word} {verb_word} {prep_phrase}.")
            
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
            
            if qty == 1:
                  words = single_determiner_list
            else:
                  words = plural_determiner_list

            word = random.choice(words)
            determiner_word = word

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
            
            # Check for "past" tense, if true execute the following code
            if   "past" in tense_qty:
                  words = past_verb_list
                  verb_word = random.choice(words)
            # Check for "future" tense, if true execute the following code
            elif "future" in tense_qty:
                  words = single_present_verb_list
                  word  = random.choice(words)
                  verb_word = (f"will {word}")
            # Check for "present" tense, if true execute the following code
            elif "present" in tense_qty and 1 in tense_qty:
                  words = single_present_verb_list
                  verb_word = random.choice(words)
            # If none of the above tenses are true, execute the following code
            else:
                  words = single_present_verb_list
                  verb_word = random.choice(words)
            # Check for "past" tense, if true execute the following code
            return verb_word
      


    def get_preposition():
            """Return a randomly chosen preposition
            from this list of prepositions:
                "about", "above", "across", "after", "along",
                "around", "at", "before", "behind", "below",
                "beyond", "by", "despite", "except", "for",
                "from", "in", "into", "near", "of",
                "off", "on", "onto", "out", "over",
                "past", "to", "under", "with", "without"
            Return: a randomly chosen preposition.
            """
            words = preposition_list

            prep_word = random.choice(words)

            return prep_word


    def get_prepositional_phrase(quantity):
            """Build and return a prepositional phrase composed
            of three words: a preposition, a determiner, and a
            noun by calling the get_preposition, get_determiner,
            and get_noun functions.
            Parameter
                quantity: an integer that determines if the
                    determiner and noun in the prepositional
                    phrase returned from this function should
                    be single or pluaral.
            Return: a prepositional phrase.
            """
            
            preposition_word = get_preposition()
            determiner_word  = get_determiner(quantity)
            noun_word        = get_noun(quantity)

            prep_phrase = (f"{preposition_word} {determiner_word} {noun_word}")

            return prep_phrase
    


    def get_adjective():
            """Return a randomly chosen adjective
            from a list of prepositions:
            """
            words = adjective_list

            adjective_word = random.choice(words)

            return adjective_word
    


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
      
      

      