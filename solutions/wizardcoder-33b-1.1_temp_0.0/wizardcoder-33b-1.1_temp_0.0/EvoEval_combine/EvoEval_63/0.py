
def sort_planets(planet1: str, planet2: str, order: str) -> str:
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return 'Invalid'
    order_list = order.split()
    if len(order_list) != len(set(order_list)) or not all((0 <= int(i) <= 7 for i in order_list)):
        return 'Invalid'
    (index1, index2) = (planets.index(planet1), planets.index(planet2))
    if index1 > index2:
        (index1, index2) = (index2, index1)
    result = [int(i) for i in order_list if index1 < planets.index(planets[int(i)]) < index2]
    return ' '.join((str(i) for i in sorted(result, key=order_list.index)))