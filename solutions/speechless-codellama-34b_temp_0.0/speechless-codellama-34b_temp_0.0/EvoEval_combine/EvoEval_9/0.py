def planet_to_roman_distance(planet1, planet2):
    planets = {'mercury': 1, 'venus': 2, 'earth': 3, 'mars': 4, 'jupiter': 5, 'saturn': 6, 'uranus': 7, 'neptune': 8}
    roman_numerals = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii'}
    if planet1 not in planets or planet2 not in planets:
        return {}
    planet1_position = planets[planet1.lower()]
    planet2_position = planets[planet2.lower()]
    if planet1_position > planet2_position:
        (planet1_position, planet2_position) = (planet2_position, planet1_position)
    result = {}
    for (planet, position) in planets.items():
        if planet1_position < position < planet2_position:
            result[planet] = roman_numerals[position]
    return result