def planet_to_roman_distance(planet1, planet2):
    planets = {'mercury': 'i', 'venus': 'ii', 'earth': 'iii', 'mars': 'iv', 'jupiter': 'v', 'saturn': 'vi', 'uranus': 'vii', 'neptune': 'viii'}
    planet_order = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    planet1 = planet1.lower()
    planet2 = planet2.lower()
    if planet1 not in planets or planet2 not in planets:
        return {}
    start = planet_order.index(planet1)
    end = planet_order.index(planet2)
    if start > end:
        (start, end) = (end, start)
    result = {}
    for i in range(start + 1, end):
        result[planet_order[i]] = planets[planet_order[i]]
    return result