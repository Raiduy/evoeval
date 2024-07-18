
def bf(planet1, planet2):
    solar_system = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in solar_system or planet2 not in solar_system:
        return ()
    planet1_index = solar_system.index(planet1)
    planet2_index = solar_system.index(planet2)
    if planet1_index < planet2_index:
        return tuple(solar_system[planet1_index + 1:planet2_index])
    else:
        return tuple(solar_system[planet2_index + 1:planet1_index])