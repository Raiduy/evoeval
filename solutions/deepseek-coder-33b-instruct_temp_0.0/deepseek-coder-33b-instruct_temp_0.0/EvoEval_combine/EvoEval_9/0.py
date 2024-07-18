def planet_to_roman_distance(planet1, planet2):
    planet_distance = {'mercury': 1, 'venus': 2, 'earth': 3, 'mars': 4, 'jupiter': 5, 'saturn': 6, 'uranus': 7, 'neptune': 8}
    roman_numerals = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii'}
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    if planet1 not in planet_distance or planet2 not in planet_distance:
        return {}
    planet1_distance = planet_distance[planet1]
    planet2_distance = planet_distance[planet2]
    if planet1_distance > planet2_distance:
        (planet1_distance, planet2_distance) = (planet2_distance, planet1_distance)
    planets_between = {planet: roman_numerals[distance] for (planet, distance) in planet_distance.items() if planet1_distance < distance < planet2_distance}
    return planets_between