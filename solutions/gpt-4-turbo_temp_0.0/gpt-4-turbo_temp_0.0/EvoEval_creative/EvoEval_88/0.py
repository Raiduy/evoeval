def planet_population(dict_of_planets):
    density_dict = {}
    for (planet, features) in dict_of_planets.items():
        if features[0] is not None and features[1] is not None:
            population_density = features[0] / features[1]
            density_dict[planet] = round(population_density, 2)
    return density_dict