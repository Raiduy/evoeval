def planet_population(dict_of_planets):
    result = {}
    for (planet, data) in dict_of_planets.items():
        (population, size) = data
        if population is None or size is None:
            continue
        if population <= 0 or size <= 0:
            continue
        density = round(population / size, 2)
        result[planet] = density
    return result