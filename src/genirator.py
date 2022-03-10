from resorces import Planet, Moon
from random import randint, choice

moon_names = ["Luna", "Libram", "Corax"]
planet_names = ["Signus", "Baal", "corvus"]

def main():

    print(choice(planet_names))

main()

def generate_planet(self):
    name = randint(0, 2)
    size = randint(10000, 1e20)

    return_planet = Planet(name, size)

def generate_moon(self):
    name = randint(0, 2)
    if name == 0:

        size = randint(100, 5000)

        return_moon = Moon(name, size)
