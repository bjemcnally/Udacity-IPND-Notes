# Greatest Quiz

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

# My answer

def greatest2(list_of_numbers):
    biggest = 0
    for each in list_of_numbers:
        if each > biggest:
            biggest = each
    return biggest

print greatest2([4,23,1])
#>>> 23
print greatest2([])
#>>> 0

# My answer with shortcuts...

def greatest(list_of_numbers):
    if len(list_of_numbers) > 0:
        return max(list_of_numbers)
    else:
        return 0

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

# Video answer... the same as the first answer!

    
