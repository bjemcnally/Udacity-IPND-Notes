# Putting It All Together Quiz

# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# My answer    
        
def play_game(ml_string, parts_of_speech_list):    
    replaced = []
    string_list = ml_string.split(" ")
    for each in string_list:
        check = word_in_pos(each, parts_of_speech_list)
        if check != None:
            fixed = each.replace(check, "corgi")
            replaced.append(fixed)
        else:
            replaced.append(each)
    return " ".join(replaced)

# this worked
    
print play_game(test_string, parts_of_speech)       

# Video answer

ml_string2 = "PLACE is really ADJECTIVE!"
parts_of_speech2 = ["PLACE", "ADJECTIVE"]

def play_game2(ml_string2, parts_of_speech2):
    replaced2 = []
    ml_string2 = ml_string2.split()
    for word in ml_string2:
        replacement = word_in_pos(word, parts_of_speech2)
        if replacement != None:
            # add this to prompt user:
            # user_input = raw_input("Type in a: " + replacement)
            word = word.replace(replacement, "corgi") # then swap out corgi with user_input
            replaced2.append(word)
        else:
            replaced2.append(word)
    replaced2 = " ".join(replaced2)
    return replaced2

print play_game2(ml_string2, parts_of_speech2)

# Essentially identical to mine! (WOOHOO!)


