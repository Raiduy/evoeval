
def planet_vowel_count(planet1, planet2):
    """
    There are eight planets in our solar system: the closest to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.

    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return an integer representing the number of vowels 
    in the names of the planets whose orbits are located between the orbit of 
    planet1 and the orbit of planet2, sorted by the proximity to the sun. 

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given planet name.

    If planet1 or planet2 are not correct planet names, the function should return 0.

    Examples
    planet_vowel_count("Jupiter", "Neptune") ==> 5  # (Saturn = 2, Uranus = 3)
    planet_vowel_count("Earth", "Mercury") ==> 2  # (Venus = 2)
    planet_vowel_count("Mercury", "Uranus") ==> 10  # (Venus = 2, Earth = 2, Mars = 1, Jupiter = 3, Saturn = 2)
    """
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return 0
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 > index2:
        (index1, index2) = (index2, index1)
    between_planets = planets[index1 + 1:index2]
    vowel_count = 0
    for planet in between_planets:
        for char in planet:
            if char.lower() in 'aeiou' or (char.lower() == 'y' and char == planet[-1]):
                vowel_count += 1
    return vowel_count