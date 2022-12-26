# Print a string
print('Hello Word')

# Create a class


class Puppy:  # create a class called Puppy
    # Define variables for the class (Similar to constructor in JavaScript).
    def __init__(self, name, toy):
        self.name = name  # Initialize received values.
        self.toy = toy


zion = Puppy('zion', 'lizard')  # Create instance member of class Puppy.
print(zion.name)
print()
