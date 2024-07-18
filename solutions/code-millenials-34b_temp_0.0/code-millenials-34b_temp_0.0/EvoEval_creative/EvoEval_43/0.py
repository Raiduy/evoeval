def space_travel(distance, speed, fuel, planet_gravity, spaceship_weight):
    fuel_consumption = spaceship_weight * planet_gravity * 0.1
    trip_duration = distance / speed
    if fuel < trip_duration:
        return 'Insufficient fuel'
    else:
        remaining_fuel = fuel - trip_duration
        return round(remaining_fuel, 2)