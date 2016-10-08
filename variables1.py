# Variables 1

# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

mary = "Mary"
# Your code goes here
randa = mary
katie = randa
salwa = katie
kathleen = salwa
gabriel = kathleen



# In South America, the alias Kathleen is known as the alias Gabriel, this means that:
gabriel = kathleen

# Test to see if all of these variables will print out the string "Mary"
print gabriel
print kathleen
print salwa
print katie
print randa
print mary

# My answer was correct!

# Finding Strings Quiz
# use string.find method to find instances of NOUN and VERB occur (I've already done this earlier in this test, this should be easy! Hopefully...)

# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find at https://goo.gl/Pde1nZ or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

noun_position = text.find("N")
verb_position = text.find("V")

# this worked!

# Find 2 Quiz

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

# ENTER CODE BELOW HERE
print text.find('zip', text.find('zip') + 1)

# This worked! Woohoo! First try!

# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function

# answer from video

first_zip = text.find('zip')
print text.find('zip', first_zip + 1)

# the other answer from the quiz was my answer

# Replacing Strings Quiz

# use replace method!

sentence = "I am a NOUN"
print sentence.replace("NOUN", "bird")

# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace('NOUN','duck')
sentence = sentence.replace('VERB','waddle')
print sentence

# this worked!












