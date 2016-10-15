# Strategy: Examine Error Messages

# A small change will fix the crashing bug in printInches.

def printExample(a, b):
    print a + b
    
def printInches(n):
    print str(n) + " inches" # without str() this code does not function

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)

# Strategy: Working from a Working Example

# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

def bracket(text):
    return '[' + text + ']'

def boldwrap(text): # needed to add the colon here to fix the code!
    return '<b>' + text + '</b>'

print boldwrap('This is an important message.')

# Strategy: Check Intermediate Results

# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

# MY ANSWER

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub) # this returns -1 if sub is not found!
    if location == -1:
        return somestring
    else: 
        length = len(sub)
        part_before = somestring[:location]
        part_after = somestring[location + length:]
        return part_before + part_after


# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"

# Video Answer: the same as mine, but without else:



