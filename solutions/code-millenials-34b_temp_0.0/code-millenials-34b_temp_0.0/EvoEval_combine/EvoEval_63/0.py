
def sort_planets(planet1: str, planet2: str, order: str) -> str:
    planets_order = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}
    planets_names = {'Mercury': 0, 'Venus': 1, 'Earth': 2, 'Mars': 3, 'Jupiter': 4, 'Saturn': 5, 'Uranus': 6, 'Neptune': 7}
    if planet1 not in planets_names or planet2 not in planets_names:
        return 'Invalid'
    order_list = order.split()
    if len(order_list) != 8 or any((planet not in planets_order for planet in order_list)):
        return 'Invalid'
    planet1_order = planets_names[planet1]
    planet2_order = planets_names[planet2]
    if planet1_order > planet2_order:
        (planet1_order, planet2_order) = (planet2_order, planet1_order)
    return ' '.join((planet for planet in order_list if planet1_order < planets_order[planet] < planet2_order))