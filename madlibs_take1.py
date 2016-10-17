# Mad Libs: Take One

sentence = "I am a NOUN"

processed = ""

# check if a word = "NOUN" or "VERB", and replace with a random word, if not keep the word and move on!

# Alternative: go through the "sentence" string one character at a time with a box that is 4 characters wide until you find NOUN, etc


# Word Transformer Quiz

# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    # MY ANSWER
    if word == "NOUN":
        return random_noun()
    if word == "VERB":
        return random_verb()
    return word[0]

    # THIS WORKED!

# Video ANSWER is identical to mine

# Process Mad Lib Quiz

# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    processed = ""
    # MY FIRST ANSWER
    # new_noun = mad_lib.replace("NOUN",random_noun())
    # processed = new_noun.replace("VERB", random_verb())
    # return processed
    # this would work, but doesn't use word_transformer

    # SECOND ANSWER
    # start = 0
    # end = len(mad_lib) - 3
    # while start <= end:
        # four_letters = mad_lib[start:(start + 4)]
        # processed += word_transformer(four_letters)
        # start = start + 1
    # this is not working either... try again tomorrow!


    
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)






