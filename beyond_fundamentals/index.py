import multiply_module
# Creating list. Also called array in JavaScript
cities = [
    'Tokyo',
    'Dakar',
    'Mumbai',
    'Buenos Aires',
]

# Creating dictionary. Also called object in JavaScript.
california_symbols = {
    'bird': 'California quail',
    'animal': 'Grizzly bear',
    'flower': 'California poppy',
    'fruit': 'Avocado',
}

# Access an element in a list.
print(cities[1])

# Access an element in a dictionary.
print(california_symbols['flower'])

# Using multiply function from multiply_module.
multiply_module.multiply(3, 10)
