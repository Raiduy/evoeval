def space_travel(distance, speed, fuel, planet_gravity, spaceship_weight):
    fuel_consumption = spaceship_weight * planet_gravity * 0.1
    trip_duration = distance / speed
    if fuel >= trip_duration:
        remaining_fuel = round(fuel - trip_duration - fuel_consumption, 2)
        return remaining_fuel
    else:
        return 'Insufficient fuel'