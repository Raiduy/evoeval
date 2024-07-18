
def sort_planets(planet1: str, planet2: str, order: str) -> str:
    planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planet_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']
    if planet1 not in planet_names or planet2 not in planet_names:
        return 'Invalid'
    order_list = order.split()
    if len(order_list) != len(set(order_list)) or not all((i in planet_numbers for i in order_list)):
        return 'Invalid'
    planet1_index = planet_names.index(planet1)
    planet2_index = planet_names.index(planet2)
    if planet1_index < planet2_index:
        planets_between = order_list[planet1_index + 1:planet2_index]
    else:
        planets_between = order_list[planet2_index + 1:planet1_index]
    return ' '.join(planets_between)