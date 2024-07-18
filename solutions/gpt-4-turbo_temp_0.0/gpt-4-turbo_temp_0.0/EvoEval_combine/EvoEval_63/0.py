
def sort_planets(planet1: str, planet2: str, order: str) -> str:
    planet_to_num = {'Mercury': 'zero', 'Venus': 'one', 'Earth': 'two', 'Mars': 'three', 'Jupiter': 'four', 'Saturn': 'five', 'Uranus': 'six', 'Neptune': 'seven'}
    num1 = planet_to_num.get(planet1)
    num2 = planet_to_num.get(planet2)
    if num1 is None or num2 is None:
        return 'Invalid'
    order_list = order.split()
    if len(order_list) != len(set(order_list)) or set(order_list) != set(planet_to_num.values()):
        return 'Invalid'
    index1 = order_list.index(num1)
    index2 = order_list.index(num2)
    if index1 > index2:
        (index1, index2) = (index2, index1)
    return ' '.join(order_list[index1 + 1:index2])