def planet_population(dict_of_planets):
    result = {}
    for (planet, features) in dict_of_planets.items():
        if None in features or len(features) != 2:
            continue
        (population, size) = features
        if size == 0:
            continue
        density = round(population / size, 2)
        result[planet] = density
    return result