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