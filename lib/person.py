#!/usr/bin/env python3

class Person:
    def __init__(self, name, Planet="Earth", species="Human"):
        self.name = name
        self.Planet = Planet
        self.species = species

zic = Person("zic_808","Cybertron", "Saiyan")
print (zic.name)
print (zic.Planet)
print(zic.species)

