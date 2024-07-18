
def planet_vowel_count(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return 0
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 > index2:
        (index1, index2) = (index2, index1)
    vowel_count = 0
    for planet in planets[index1 + 1:index2]:
        for char in planet.lower():
            if char in 'aeiou' or (char == 'y' and planet.endswith('y')):
                vowel_count += 1
    return vowel_count