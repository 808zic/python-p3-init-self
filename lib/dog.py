#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed= "Mutt"):
        self.name = name
        self.breed = breed


fido = Dog("Fido", "German Shepherd")
fido.name
fido.breed

shazzy = Dog("Shazzy", "Chihuahua")
shazzy.name
shazzy.breed
        
   

   










#NOTE:To provide objects with unique attributes upon instantiation, we use the __init__ method.
#__init__
'''
The __init__ method belongs to every class and is invoked when you initialize a class
__init__ can also be modified to take more arguments. This allows us to customize the behavior of unique objects:
class Dog:
    def __init__(self, name):
    
'''

#self
#Note: self is the same type of object as fido! As a matter of fact, it is fido!
'''
The self keyword refers to the instance, or object, that the showing_self() method is being called on.

'''

#NOTE:Now that we know that __init__ contains code that runs whenever we initialize a new object and that
# the self that is passed to each method is a reference to the initialized object, let's make some unique dogs:
