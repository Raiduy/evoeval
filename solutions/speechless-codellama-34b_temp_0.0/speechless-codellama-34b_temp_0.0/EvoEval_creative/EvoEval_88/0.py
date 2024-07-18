def planet_population(dict_of_planets):
    result = {}
    for (planet, data) in dict_of_planets.items():
        if len(data) == 2 and data[0] is not None and (data[1] is not None):
            result[planet] = round(data[0] / data[1], 2)
    return result