def binary_planet_distance(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ''
    else:
        planet1_index = planets.index(planet1)
        planet2_index = planets.index(planet2)
        if planet1_index > planet2_index:
            (planet1_index, planet2_index) = (planet2_index, planet1_index)
        planets_in_between = planets[planet1_index + 1:planet2_index]
        binary_string = bin(len(planets_in_between))[2:]
        return 'bd' + binary_string + 'bd'