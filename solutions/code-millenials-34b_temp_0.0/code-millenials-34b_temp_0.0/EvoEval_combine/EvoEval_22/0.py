def binary_planet_distance(planet1, planet2):
    planets_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets_order or planet2 not in planets_order:
        return ''
    planet1_index = planets_order.index(planet1)
    planet2_index = planets_order.index(planet2)
    if planet1_index > planet2_index:
        (planet1_index, planet2_index) = (planet2_index, planet1_index)
    planets_between = planets_order[planet1_index + 1:planet2_index]
    binary_string = 'bd' + ''.join((format(i, 'b') for i in range(1, len(planets_between) + 1))) + 'bd'
    return binary_string