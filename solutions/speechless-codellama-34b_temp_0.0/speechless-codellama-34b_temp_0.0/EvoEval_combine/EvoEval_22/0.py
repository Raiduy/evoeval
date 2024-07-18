def binary_planet_distance(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ''
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    if planet1_index > planet2_index:
        (planet1_index, planet2_index) = (planet2_index, planet1_index)
    planets_between = planets[planet1_index + 1:planet2_index]
    binary_string = 'bd' + ''.join(['1' if planet in planets_between else '0' for planet in planets]) + 'bd'
    return binary_string