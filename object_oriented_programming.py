# Classes - A framework to describe an Object

# Instantiating a class:
class Cat:

    # Add a variable that is available to anything in this Class
    has_soul = False

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    # Making other methods for our Cat class
    def speak(self):
        print(f'My name is {self.name}')

rupert = Cat('Rupert', 14, 'grey')

print(rupert.name)

rupert.speak()

lumpy = Cat('Lumpy', 12, 'black')

lumpy.speak()

