# Classes - A framework to describe an Object

class Animal:
    def __init__(self, number_eyes):
        self.number_eyes = number_eyes

    def breathe(self):
            print("Inhale, exhale")

    def eat(self):
            print("I'm eating")

# Instantiating a class:
class Cat(Animal): # Cat inherits from the super class Animal

    # Add a variable that is available to anything in this Class
    has_soul = False

    def __init__(self, name, age, color):
        super().__init__(2)
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

# Inheritance (see line 3)

cyclops_goat = Animal(1)

print(rupert.number_eyes)

kitten = Cat('Potato', 0, 'orange')

print(kitten.number_eyes)

