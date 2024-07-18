def space_travel(distance, speed, fuel, planet_gravity, spaceship_weight):
    trip_duration = distance / speed
    if fuel < trip_duration:
        return 'Insufficient fuel'
    fuel_consumption = spaceship_weight * planet_gravity * 0.1 * trip_duration
    remaining_fuel = fuel - fuel_consumption
    return round(remaining_fuel, 2)