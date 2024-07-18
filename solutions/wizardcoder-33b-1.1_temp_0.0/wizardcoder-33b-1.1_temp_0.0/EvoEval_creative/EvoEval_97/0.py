def alien_invasion(alien, humans):
    if not isinstance(alien, str) or not isinstance(humans, dict):
        return []
    continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    invasion_order = ['Asia', 'Africa', 'Europe', 'North America', 'South America']
    encounter_order = []
    for continent in invasion_order:
        for (human, place) in humans.items():
            if place == continent:
                encounter_order.append(human)
    return encounter_order