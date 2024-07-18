
def planet_vowel_count(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    vowels = ['a', 'e', 'i', 'o', 'u']
    if planet1 not in planets or planet2 not in planets:
        return 0
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    if planet1_index > planet2_index:
        (planet1_index, planet2_index) = (planet2_index, planet1_index)
    planet_subset = planets[planet1_index + 1:planet2_index]
    vowel_count = 0
    for planet in planet_subset:
        for char in planet:
            if char.lower() in vowels:
                vowel_count += 1
    return vowel_count