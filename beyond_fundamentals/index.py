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

# Accessing number inputs.
# num = int(input('Enter a number: '))
# print(f'square of {num} is {num * num}')

# Working with strings.
first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize'

print(first_name.capitalize())
print(last_name.capitalize())

# print the characters from index 7 to the end of string.
print(f'Award text: {note[7:]}.')
