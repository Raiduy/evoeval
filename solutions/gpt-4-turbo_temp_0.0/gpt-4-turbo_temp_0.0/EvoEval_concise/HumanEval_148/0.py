
def bf(planet1, planet2):
    """
    Given two planet names (planet1 and planet2), this function returns a tuple of all planets 
    located between the orbits of planet1 and planet2, sorted by their proximity to the sun. 
    Planets considered are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. 
    If invalid planet names are given, the function returns an empty tuple.
    """
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 < index2:
        return tuple(planets[index1 + 1:index2])
    else:
        return tuple(planets[index2 + 1:index1])