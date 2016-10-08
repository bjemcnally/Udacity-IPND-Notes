pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres.'

print pythagoras.find('string') # returns 40
print pythagoras[40:] # this verifies the result from above
print pythagoras.find('T') # returns 0
print pythagoras.find('sphere') # returns 86
print pythagoras[86:]
print pythagoras.find('algebra') # returns -1, because the string was not found

# Testing Quiz

# Which of the following evaluate to -1:
# My answer:
# "Test".find('te')
# 'west'.find('test')
# I was correct, Python is case sensitive!

# Testing 2 Quiz

# For any string, s, which of the following always has the value 0?
# My answer:
# 's'.find('s')
# I was wrong...
# s.find(s + '!!!') + 1 is also correct, it will return -1 + 1 = 0!
# s.find('') is also correct, according to Python, every string begins with an empty string (what?)
# s.find(s), I misunderstood this one, it's like saying:
# s = 'hello', s.find('hello')

# Finding with Numbers

my_string = "hello, hello"
print my_string.find('h') # should return 0 for the first occurrence
print my_string.find('h', 1) # should return 7 (it does)

# example from video
danton = "De l'audace, encore de l'audace, toujours de l'audace."
print danton.find('audace') # return 5
print danton.find('audace', 0) # return 5
print danton.find('audace', 5) # still returns 5 because it started looking at position 5
print danton.find('audace', 6) # will now return the start of the next audace, 25
print danton[25:] # this confirms that result, etc.
# final audace is at position 47...
print danton.find('audace', 48) # will return -1, because it does not exist at or after position 48

# Python Programming 1 Quiz

# print number of hours in 7 weeks
print 7 * 7 * 24 # can also use variables to store each value

# Strings Quiz

# Given any string s, which of the following always have the same value as s?
# remember that s could be '' (an empty string)
# My Answer:
# ('a' + s)[1:] = s, this will add a to beginning of string, but looks to use characters in new string beginning after the a and going to the end
# s[0] + s[1:] = s 
# s + '' = s 
# s [0:]

# I was wrong, if s is an empty string '', s[0] + s[1:] would give an error because there is no character at position 0
# s[0:] does work because it's looking for the characters between 0 and the end???

# Given
s = 'udacity' # and
t = 'bodacious'
# Write Python code that prints out udacious without using any quote characters in your code

print s[0:5] + t[6:] # there are many ways to do this, but this worked!

# answer from video:
print s[:5] + t[6:]
# to avoid counting above 4:
print s[:-2] + t[-3:]

# String slicing question
# no notes here bc this was easy

# Slicing Multiple Strings question
# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
# below is my answer, avoid counting! haha
substring1 = sentence[0:2]
substring2 = sentence[6:sentence.find('V')]
substring3 = sentence[sentence.find('B') + 1:]

# answer from video
substring1 = sentence[:2] # remember you can leave left hand side blank here!
substring2 = sentence[6:30]
substring3 = sentence[34:] # used 30 + length of verb (4)

# String Concatenation question

# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "cat" # your noun here
verb_replacement = "jump" # your verb here

new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
print new_sentence
# your code here

# answer from video for the concantenation step:
new_sentence1 = ''
new_sentence1 += substring1
new_sentence1 += noun_replacement
new_sentence1 += substring2
new_sentence1 += verb_replacement
new_sentence1 += substring3
print new_sentence1

# Variables 1 question is in new .py

