def planet_population(dict_of_planets):
    result = {}
    for (planet, features) in dict_of_planets.items():
        (population, size) = features
        if population is not None and size is not None and (size != 0):
            density = round(population / size, 2)
            result[planet] = density
    return result