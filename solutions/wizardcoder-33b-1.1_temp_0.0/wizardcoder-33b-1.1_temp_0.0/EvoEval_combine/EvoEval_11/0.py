
def planet_vowel_count(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    vowels = ['a', 'e', 'i', 'o', 'u']
    if planet1 not in planets or planet2 not in planets:
        return 0
    start = min(planets.index(planet1), planets.index(planet2))
    end = max(planets.index(planet1), planets.index(planet2))
    count = 0
    for planet in planets[start + 1:end]:
        for char in planet:
            if char.lower() in vowels:
                count += 1
    return count