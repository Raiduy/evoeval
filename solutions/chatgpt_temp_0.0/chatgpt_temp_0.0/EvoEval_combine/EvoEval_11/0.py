
def planet_vowel_count(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    vowels = ['a', 'e', 'i', 'o', 'u']
    if planet1 not in planets or planet2 not in planets:
        return 0
    start_index = planets.index(planet1)
    end_index = planets.index(planet2)
    if start_index > end_index:
        (start_index, end_index) = (end_index, start_index)
    count = 0
    for i in range(start_index + 1, end_index):
        planet = planets[i]
        if planet[-1] in vowels:
            count += 1
        for vowel in vowels:
            count += planet.count(vowel)
    return count