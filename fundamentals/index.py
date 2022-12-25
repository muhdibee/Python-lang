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
name = input('Whats your name? ')
print('Nice to meet you. ', name)
response = input('Are you enjoying the course.')

if response == 'Yes':
    print("That's good to hear!")
else:
    print("Oh no! That's sad to hear.")
