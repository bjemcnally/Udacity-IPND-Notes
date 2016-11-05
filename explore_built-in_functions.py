# Ppick a built-in Python function
# Use that function in a new program and share the following on this forum:
# -- Which function did you use?
# -- What does your program do?
# -- What problems (if any) did you run into?

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def is_bigger_than_5(x):
    if x > 5:
        return True
    else:
        return False

print filter(is_bigger_than_5, list_of_numbers)