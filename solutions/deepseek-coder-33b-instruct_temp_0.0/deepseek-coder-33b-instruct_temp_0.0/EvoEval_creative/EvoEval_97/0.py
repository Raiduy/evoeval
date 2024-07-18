def alien_invasion(alien, humans):
    if not isinstance(alien, str) or not isinstance(humans, dict):
        return []
    continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    alien_encounters = []
    for continent in continents:
        for (human, continent_residence) in humans.items():
            if continent_residence == continent:
                alien_encounters.append(human)
    return alien_encounters