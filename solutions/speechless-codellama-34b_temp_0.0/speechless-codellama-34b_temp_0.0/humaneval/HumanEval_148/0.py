
def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        planet1_index = planets.index(planet1)
        planet2_index = planets.index(planet2)
        if planet1_index < planet2_index:
            return tuple(planets[planet1_index+1:planet2_index])
        else:
            return tuple(planets[planet2_index+1:planet1_index])
