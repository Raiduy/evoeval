
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    if planet1_index == -1 or planet2_index == -1:
        return ()
    else:
        return tuple(planets[planet1_index + 1:planet2_index])