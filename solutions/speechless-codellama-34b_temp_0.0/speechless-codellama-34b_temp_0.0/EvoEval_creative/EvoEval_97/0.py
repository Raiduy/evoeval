def alien_invasion(alien, humans):
    if not isinstance(alien, str) or not isinstance(humans, dict):
        return []
    continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    encounter_order = []
    for continent in continents:
        for (human, human_continent) in humans.items():
            if human_continent == continent:
                encounter_order.append(human)
    return encounter_order