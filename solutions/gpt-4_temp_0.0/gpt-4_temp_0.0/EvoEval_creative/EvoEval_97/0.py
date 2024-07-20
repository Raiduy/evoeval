def alien_invasion(alien, humans):
    if not isinstance(alien, str) or not isinstance(humans, dict):
        return []
    continents_order = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    encounter_order = []
    for continent in continents_order:
        for (human, location) in humans.items():
            if location == continent:
                encounter_order.append(human)
    return encounter_order