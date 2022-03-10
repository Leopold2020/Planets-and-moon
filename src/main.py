
import marshal
from resorces import Planet, Moon

def main():
    Tellus = Planet("Tellus", 5.101e8)
    Mars = Planet("Mars", 1.448e8)
    Jupiter = Planet("Jupiter", 6.142e10)

    Luna = Moon("Luna", 1.46e7)
    Phobos = Moon("Phobos", 1548.3)
    Deimos = Moon("Deimos", 495.15)
    Europa = Moon("Eropa", 3.09e7)
    Ganyamede = Moon("Ganyamede", 8.72e7)

    Tellus.add_moon(Luna)
    Mars.add_moon(Phobos)
    Mars.add_moon(Deimos)
    Jupiter.add_moon(Europa)
    Jupiter.add_moon(Ganyamede)

    Luna.add_orbit(Tellus)
    Phobos.add_orbit(Mars)
    Deimos.add_orbit(Mars)
    Europa.add_orbit(Jupiter)
    Ganyamede.add_orbit(Jupiter)

    Tellus.print_moons()
    Jupiter.print_moons()

    Mars.certain_size(1000)


if __name__ == "__main__":
    main()


    