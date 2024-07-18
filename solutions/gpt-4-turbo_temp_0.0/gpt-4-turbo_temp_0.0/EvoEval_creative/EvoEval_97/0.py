def alien_invasion(alien, humans):
    if not isinstance(alien, str) or not isinstance(humans, dict):
        return []
    invasion_order = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    continent_group = {continent: [] for continent in invasion_order}
    for (human, continent) in humans.items():
        if continent in continent_group:
            continent_group[continent].append(human)
    sorted_humans = []
    for continent in invasion_order:
        sorted_humans.extend(continent_group[continent])
    return sorted_humans