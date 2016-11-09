# Using dictionaries

elements = { 'hydrogen': 1, 'helium': 2, 'carbon': 6 }

print elements  # whole dictionary
print elements['hydrogen']  # one element's value
print elements['carbon']  # same

# print elements['lithium'] 
# this will throw a KeyError

print 'lithium' in elements  # evaluates to False

elements['lithium'] = 3  # this will add an elements

print elements

elements['nitrogen'] = 8

print elements['nitrogen']

# whoops, nitrogen's atomic number is 7...abs
elements['nitrogen'] = 7

print elements['nitrogen']