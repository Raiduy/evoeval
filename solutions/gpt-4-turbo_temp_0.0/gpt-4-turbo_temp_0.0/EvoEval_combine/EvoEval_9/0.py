def planet_to_roman_distance(planet1, planet2):
    planet_positions = {'mercury': 1, 'venus': 2, 'earth': 3, 'mars': 4, 'jupiter': 5, 'saturn': 6, 'uranus': 7, 'neptune': 8}
    roman_numerals = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii'}
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    if planet1 not in planet_positions or planet2 not in planet_positions:
        return {}
    pos1 = planet_positions[planet1]
    pos2 = planet_positions[planet2]
    start_pos = min(pos1, pos2) + 1
    end_pos = max(pos1, pos2)
    planets_between = {planet: roman_numerals[position] for (planet, position) in planet_positions.items() if start_pos <= position < end_pos}
    return planets_between