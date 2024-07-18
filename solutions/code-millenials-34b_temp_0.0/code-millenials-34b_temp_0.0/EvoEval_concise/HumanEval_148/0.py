
def bf(planet1, planet2):
    planets_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets_order or planet2 not in planets_order:
        return ()
    planet1_index = planets_order.index(planet1)
    planet2_index = planets_order.index(planet2)
    if planet1_index < planet2_index:
        return tuple(planets_order[planet1_index + 1:planet2_index])
    else:
        return tuple(planets_order[planet2_index + 1:planet1_index])