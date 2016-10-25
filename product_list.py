# Product List Quiz

# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

# My answer

def product_list(list_of_numbers):
    product = 1
    for each in list_of_numbers:
        product *= each
    return product
# This worked, essentially the same as the given answer

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1