def space_travel(distance, speed, fuel, planet_gravity, spaceship_weight):
    """
    Given the distance of a planet from Earth in light years, the speed of the spaceship in light years per year, the amount of fuel in the spaceship in years, the gravity of the planet and the weight of the spaceship.
    Fuel consumption is computed as spaceship_weight * planet_gravity * 0.1 per year.
    Return the remaining fuel rounded to 2 decimal points once the spaceship reaches the planet, if it is possible for the spaceship to reach the planet.
    Otherwise, return 'Insufficient fuel'.
    The spaceship can reach the planet if the amount of fuel is greater than or equal to the duration of the trip (distance divided by speed).
    The remaining fuel is calculated by subtracting the fuel consumption of the trip from the initial amount of fuel.
    Note: The spaceship travels at a constant speed and the fuel consumption is constant unless otherwise mentioned.

    Example:
    space_travel(4.22, 0.5, 10, 9.8, 100) returns 'Insufficient fuel'
    space_travel(2.5, 1, 2, 3.7, 1.5) returns 0.61
    """
    trip_duration = distance / speed
    fuel_consumption = round(spaceship_weight * planet_gravity * 0.1 * trip_duration, 2)
    if fuel < trip_duration:
        return 'Insufficient fuel'
    else:
        remaining_fuel = round(fuel - fuel_consumption, 2)
        return remaining_fuel