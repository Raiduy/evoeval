def planet_population(dict_of_planets):
    """
    You are given a dictionary where each key represents a planet
    and its value is a list of population features.
    Each list contains two elements: ["Population", "Size"].
    The "Population" is a positive integer representing the number of inhabitants,
    and "Size" is a positive integer representing the planet's size in square kilometers.

    Your task is to create a function that returns a new dictionary,
    where each planet is paired with its population density (population/size).
    If a planet's size or population is not provided, ignore that planet.

    If the dictionary is empty or no planet has complete data, return an empty dictionary.

    The population density should be rounded to two decimal places.

    Examples:
    planet_population({"Earth": [7000000000, 15000000], "Mars": [0, 25000000]}) == {'Earth': 466.67, 'Mars': 0.0}
    planet_population({}) == {}
    planet_population({"Jupiter": [None, 64000000]}) == {}
    planet_population({"Venus": [500000000, None]}) == {} 
    """
    result = {}
    for (planet, data) in dict_of_planets.items():
        if data[0] is not None and data[1] is not None:
            result[planet] = round(data[0] / data[1], 2)
    return result