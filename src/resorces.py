


class Planet:
    def __init__(self, name : str, size : int):
        self.name = name
        self.size = size
        self.moons = []

    def __str__(self):
        return f"Name: {self.name}\n Size: {self.size}\n Moons: {self.moons}\n"

    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size

    def get_moons(self):
        return self.moons

    def add_moon(self, moon):
        self.moons.append(moon)

    def print_moons(self):
        for moon in self.moons:
            print(moon.get_name())

    def certain_size(self, size):
        print(f"The following moons around {self.get_name()} largerthan {size} sqkm: ")
        for moon in self.moons:
            if moon.get_size() > size:
                print(moon.get_name())

class Moon:
    def __init__(self, name : str, size : int):
        self.name = name
        self.size = size
        self.orbits = None

    def __str__(self):
        return f"Name: {self.name}\n Size: {self.size}\n Orbits: {self.orbits}\n"

    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size

    def get_orbit(self):
        return self.orbits

    def add_orbit(self, orbit):
        self.orbits = orbit