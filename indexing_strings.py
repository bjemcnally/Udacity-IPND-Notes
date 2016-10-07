name = 'Dave'
print name[0]

print name[3]

# print name[4] this returns an error, "string index is out of range"

# Same value quiz
# s = "any string"
# which pairs have the same value?

# my answer:
# s[3] = s[1+1+1]
# s[0] = (s + s)[0]
# s[1] = (s + 'ity')[1] --> IF the string is only one character this is not true!
# s[-1] = (s + s)[-1]

# selecting sub sequences

word = 'assume'
print word[3] # prints u, the 4th character
print word[3:4] # also prints u 
print word[3:3] # prints nothing! (an empty line)
print word[4:6] # prints me
print word[4:] # will select position 4 to the end
print word[:2] # will start at the beginning and go through character 2 - 1
print word[:]

# Capital Udacity Quiz
# Write Python code that prints out Udacity (with capital U), given that s = 'audacity'
s = 'audacity'
print "U" + s[2:] # this worked!

# Understanding Selection Quiz
# For any string, s, which of these are always equivalent to s?

# my answer:
# s[:], prints the whole thing
# s[0:], starts at beginning, goes to end
# s[:-1], starts at beginning, goes to end <-- WRONG!

# s + s[0:-1 + 1], this will do s and adds nothing to the end!
# s[:3] + s[3:], this will print 0,1,2 and then 3 to the end, regardless of length of string 