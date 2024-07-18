
def planet_vowel_count(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    if planet1 not in planets or planet2 not in planets:
        return 0
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    if planet1_index < planet2_index:
        for planet in planets[planet1_index + 1:planet2_index]:
            for letter in planet:
                if letter in vowels:
                    vowel_count += 1
                elif letter == 'y' and planet[-1] == letter:
                    vowel_count += 1
    else:
        for planet in planets[planet2_index + 1:planet1_index]:
            for letter in planet:
                if letter in vowels:
                    vowel_count += 1
                elif letter == 'y' and planet[-1] == letter:
                    vowel_count += 1
    return vowel_count