def space_travel(distance, speed, fuel, planet_gravity, spaceship_weight):
    trip_duration = distance / speed
    fuel_consumption_per_year = spaceship_weight * planet_gravity * 0.1
    total_fuel_consumption = fuel_consumption_per_year * trip_duration
    if fuel < total_fuel_consumption:
        return 'Insufficient fuel'
    remaining_fuel = fuel - total_fuel_consumption
    return round(remaining_fuel, 2)