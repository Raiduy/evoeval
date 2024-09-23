
def sort_planets(planet1: str, planet2: str, order: str) -> str:
    planet_dict = {'Mercury': 'zero', 'Venus': 'one', 'Earth': 'two', 'Mars': 'three', 'Jupiter': 'four', 'Saturn': 'five', 'Uranus': 'six', 'Neptune': 'seven'}
    order_list = order.split()
    if planet1 not in planet_dict or planet2 not in planet_dict or len(set(order_list)) != 8 or any((i not in order_list for i in planet_dict.values())):
        return 'Invalid'
    planet1_index = order_list.index(planet_dict[planet1])
    planet2_index = order_list.index(planet_dict[planet2])
    if planet1_index < planet2_index:
        return ' '.join(order_list[planet1_index + 1:planet2_index])
    else:
        return ' '.join(order_list[planet2_index + 1:planet1_index])