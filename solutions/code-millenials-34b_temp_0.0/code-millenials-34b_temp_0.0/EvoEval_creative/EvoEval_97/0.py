def alien_invasion(alien, humans):
    continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    order = {continent: i for (i, continent) in enumerate(continents)}
    if not isinstance(alien, str) or not isinstance(humans, dict):
        return []
    human_names = sorted(humans.keys(), key=lambda x: order.get(humans[x], float('inf')))
    return human_names if human_names[0] == alien else []