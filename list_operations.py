# List Operations

stooges = ['Moe','Larry','Curly']
stooges.append('Shemp')
print stooges

# List Addition and Length

list1 = [0,1]
list2 = [2,3]
print list1 + list2

# Len Quiz

# What is the value of len(p) after running the following code:

p = [1,2]
p.append(3) # now p = [1,2,3]
p = p + [4,5] # this assigns a new value to p, therefore there are 5 elements in p
# CORRECT

# Append Quiz

# What is the value of len(p) after running the following code:

p = [1,2]
q = [3,4]
p.append(q) # p = 4 now, WRONG
# p now = [1,2,[3,4]], 3 elements in list p! CORRECT

print p # verifying my answer!

q[1] = 5 # this changes the value of q AND p! bc p = [1,2,q]
print p 

# Loops on Lists Quiz

def print_all_elements(p): # p is our input list
  i = 0
  while i < len(p): # this worked! and matched video answer
    print p[i]
    i = i + 1

# For Loops

def print_all_elements1(p):
  for e in p:
    print e

my_list = [1,2,[3,4]]
print_all_elements1(my_list)

# Notice how print_all_elements1 require less code than print_all_elements!!

# Sum List Quiz

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

# MY ANSWER
def sum_list(x):
    i = 0
    for each in x:
        i += each
    return i

# This worked!

print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134

# Video Answer

def sum_list1(p):
    result = 0
    for e in p:
        result = result + e
    return result

print sum_list1([1, 7, 4])
#>>> 12
print sum_list1([9, 4, 10])
#>>> 23
print sum_list1([44, 14, 76])
#>>> 134

# What happens if we pass an empty list?

print sum_list([]) # we get 0 because we set result = 0!

# Measure Udacity Quiz

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

# MY ANSWER
def measure_udacity(p):
    count_u = 0
    for each in p:
        if each[0] == 'U':
            count_u += 1
    return count_u
# This worked!

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

# Video answer

def measure_udacity1(U):
    count = 0
    for e in U:
        if e[0] == 'U':
            count = count + 1
        # don't need an else clause bc we won't do anything if if statement is false
    return count

print measure_udacity1(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity1(['Umika','Umberto'])
#>>> 2

print measure_udacity(['udacity','United States','union','U2'])
# test u vs U, it worked!

