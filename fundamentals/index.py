# Print hello to the screen
print("Hello")


# Collecting user input
name = input("Hi, what's your name? ")
print("Hello", name)

# Getting the type of variables.
age = 35
email_address = 'muhdibee@gmail.com'

print('Variable type for ', email_address, ' is ', type(email_address))
print('Variable type for ', age, ' is ', type(age))

# Comparison and if else statement
print('Hi!')
# name = input('Whats your name? ')
print('Nice to meet you. ', name)
response = input('Are you enjoying the course?')

if response == 'Yes' or 'yes' or 'Y' or 'y':
    print("That's good to hear!")
else:
    print("Oh no! That's sad to hear.")

# Mathematical operation:
print("2**3 = ", 2**3)
print("20//3 = ", 2//3)
print("2%3 = ", 2 % 3)
print("2+3 = ", 2+3)
print("2-3 = ", 2-3)

# Working with functions


def wash_car():
    print("1. Wash with tri-color foam")
    print("2. Rinse twice")
    print("3. Dry with large blow dryer")


wash_car()
