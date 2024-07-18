def binary_planet_distance(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ''
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 > index2:
        (index1, index2) = (index2, index1)
    count = index2 - index1 - 1
    binary_count = bin(count)[2:]
    formatted_string = f'bd{binary_count}bd'
    return formatted_string