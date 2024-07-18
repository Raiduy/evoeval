
def planet_vowel_count(planet1, planet2):
    planets_order = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    planets_vowels = [2, 2, 2, 1, 3, 2, 4, 4]
    if planet1 not in planets_order or planet2 not in planets_order:
        return 0
    planet1_index = planets_order.index(planet1)
    planet2_index = planets_order.index(planet2)
    if planet1_index > planet2_index:
        (planet1_index, planet2_index) = (planet2_index, planet1_index)
    vowel_count = 0
    for i in range(planet1_index + 1, planet2_index):
        vowel_count += planets_vowels[i]
    return vowel_count