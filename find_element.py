# Find Element Quiz

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# MY ANSWER

def find_element (p,x): # p = list, x = query
    index = 0
    for e in p:
        if e == x:
            return index
        index += 1
    return -1
# This worked!

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

# Video Answer

def find_element(p,t):
    i = 0
    while i < len(p):
        if p[i] == t:
            return i
        i = i + 1
    return -1

# or

def find_element(p,t):
    i = 0
    for e in p:
        if e == t:
            return i
        i = i + 1
    return -1 # this is essentially the same as my answer!

# Index Quiz

p = [0,1,2]
print p.index(2) # result is 2, position of #2

p = [0,1,2,2,2]
print p.index(2) # still returns 2, even though there are multiple #2s
#print p.index(3) # returns ValueError: 3 is not in list

print 3 in p # returns False
print 2 in p # returns True

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

# MY ANSWER

def find_element(p,n):
    if n in p:
        return p.index(n)
    else:
        return -1
# This worked!

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

# Video answer is the same as mine

# Alternatively:

def find_element(p,t):
    if t not in p:
        return -1
    return p.index(t)