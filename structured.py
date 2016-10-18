# Experiment with Lists Quiz

# Here's a chance to play around with lists for a bit before you continue
# Take a look at what the following code does and try to guess how it works.

print "EXAMPLE 1: Lists can contain strings"
string_list = ['HTML', 'CSS', 'Python']
print string_list

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi

print "EXAMPLE 4: Lists can contain strings AND numbers"
mixed_list = ['Hello!', 42, "Goodbye!"]
print mixed_list

print "Example 5: Lists can even contain other lists"
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print list_with_lists

# Stooges Quiz

stooges = ['Moe','Larry','Curly'] # CORRECT!

print stooges

# Days in a Month Quiz

# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    # MY ANSWER
    return days_in_month[month_number - 1] # need to subtract one to arrive at correct index!

    # This worked

print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

# Video answer is essentially the same as mine

# If we try:
# print how_many_days(13) we get an error because there aren't 13 elements in the list! i.e. list index is out of range

# Countries Quiz

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

# MY ANSWER
print countries[1][1] # this worked! and was identical to the video answer

# Relative Size Quiz

# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

# MY ANSWER
print countries[0][2] / countries[2][2]
# this worked! and was identical to the video answer

# recall that this is integer division! rounded to the nearest whole number_list

# make a number a floating point number to get a more precise answer!

# A List of Strings

p = ['H','e','l','l','o']
print p
p[0] = 'Y' # this changes the value of out list, p
print p 

# Different Stooges Quiz

# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

['Moe','Larry','Shemp']

# but does not create a new List
# object.

# MY ANSWER
stooges[2] = 'Shemp'
print stooges
# this worked, and was identical to the video answer

# Yello Mutation

s = 'Hello'
# s[0] = 'Y' 
# this does not work on strings!

p = ['H','e','l','l','o']
q = p
print p, q
p[0] = 'Y' # this changes the value of both p AND q!!
print p
print q

# Secret Agent Man Quiz

# What is the value of agent[2] after the following code runs?

spy = [0,0,7]
agent = spy # = [0,0,7]
spy[2] = agent[2] + 1 # agent[2] + 1 = 8 = spy[2] = agent[2]

# My answer = 8
print agent[2] # double check
print agent, spy
# This was correct!

# Replace Spy Quiz

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]

# MY ANSWER

def replace_spy(spy):
   spy[2] += 1
   return spy

# this seemed to work... YUP!

# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print spy
#>>> [0,0,8]

# Video answer

def replace_spy(p):
    p[2] = p[2] + 1
# return statement is unnecessary
  