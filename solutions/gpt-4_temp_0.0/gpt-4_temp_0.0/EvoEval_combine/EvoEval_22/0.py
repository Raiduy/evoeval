def binary_planet_distance(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return ''
    else:
        planet1_index = planets.index(planet1)
        planet2_index = planets.index(planet2)
        if planet1_index < planet2_index:
            distance = planet2_index - planet1_index - 1
        else:
            distance = planet1_index - planet2_index - 1
        binary_distance = bin(distance)[2:]
        return 'bd' + binary_distance + 'bd'