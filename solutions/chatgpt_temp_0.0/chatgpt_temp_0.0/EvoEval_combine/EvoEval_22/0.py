def binary_planet_distance(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ''
    start_index = planets.index(planet1)
    end_index = planets.index(planet2)
    if start_index > end_index:
        (start_index, end_index) = (end_index, start_index)
    planets_between = planets[start_index + 1:end_index]
    num_planets = len(planets_between)
    binary_str = bin(num_planets)[2:]
    return 'bd' + binary_str + 'bd'