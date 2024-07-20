
def bf(planet1, planet2):
    """
    Given two planet names (planet1 and planet2), this function returns a tuple of all planets 
    located between the orbits of planet1 and planet2, sorted by their proximity to the sun. 
    Planets considered are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. 
    If invalid planet names are given, the function returns an empty tuple.
    
    Examples:
    bf("Jupiter", "Neptune") -> ("Saturn", "Uranus")
    bf("Earth", "Mercury") -> ("Venus")
    bf("Mercury", "Uranus") -> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        start = min(planets.index(planet1), planets.index(planet2))
        end = max(planets.index(planet1), planets.index(planet2))
        return tuple(planets[start + 1:end])