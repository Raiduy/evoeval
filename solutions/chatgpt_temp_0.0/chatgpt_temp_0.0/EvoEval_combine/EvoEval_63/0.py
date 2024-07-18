
def sort_planets(planet1: str, planet2: str, order: str) -> str:
    planets = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']
    if planet1 not in planets or planet2 not in planets:
        return 'Invalid'
    order_list = order.split()
    if len(order_list) != len(set(order_list)) or any((num not in planets for num in order_list)):
        return 'Invalid'
    index1 = order_list.index(planet1)
    index2 = order_list.index(planet2)
    sorted_planets = sorted(order_list[index1 + 1:index2], key=lambda x: order_list.index(x))
    return ' '.join(sorted_planets)