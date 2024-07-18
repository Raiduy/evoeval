def planet_population(dict_of_planets):
    result = {}
    for (planet, features) in dict_of_planets.items():
        (population, size) = features
        if population is not None and size is not None:
            if size != 0:
                result[planet] = round(population / size, 2)
    return result