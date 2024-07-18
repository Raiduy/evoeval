def alien_invasion(alien, humans):
    if not isinstance(alien, str) or not isinstance(humans, dict):
        return []
    continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    encounter_order = []
    if alien not in continents:
        return []
    for continent in continents:
        for (human, location) in humans.items():
            if location == continent:
                encounter_order.append(human)
    return encounter_order