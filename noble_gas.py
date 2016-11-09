
elements = {}
elements['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elements['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602, 'noble gas': True}

print elements['H']  # print entire value associated with 'H'
print elements['H']['name']  # print one particular value from the 'H' dictionary
print elements['H']['weight']
# etc...