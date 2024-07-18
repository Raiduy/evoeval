
def sort_planets(planet1: str, planet2: str, order: str) -> str:
    planets = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}
    if planet1 not in planets or planet2 not in planets:
        return 'Invalid'
    planet1_index = planets[planet1]
    planet2_index = planets[planet2]
    if planet1_index > planet2_index:
        (planet1_index, planet2_index) = (planet2_index, planet1_index)
    order_list = order.split()
    if len(order_list) != 8 or len(set(order_list)) != 8:
        return 'Invalid'
    for planet in order_list:
        if planet not in planets:
            return 'Invalid'
    result = []
    for planet in order_list:
        planet_index = planets[planet]
        if planet_index > planet1_index and planet_index < planet2_index:
            result.append(planet)
    result.sort(key=lambda x: planets[x])
    return ' '.join(result)