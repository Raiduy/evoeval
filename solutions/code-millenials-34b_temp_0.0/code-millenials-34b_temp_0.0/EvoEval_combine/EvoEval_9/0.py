def planet_to_roman_distance(planet1, planet2):
    planets_order = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii']
    planet1_index = planets_order.index(planet1.lower())
    planet2_index = planets_order.index(planet2.lower())
    if planet1_index > planet2_index:
        return {}
    return {planets_order[i]: roman_numerals[i] for i in range(planet1_index + 1, planet2_index)}