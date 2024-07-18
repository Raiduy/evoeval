

def car_race_collision(n: int) -> int:
    """
    Calculate and return the total number of collisions that occur between two groups of 'n' cars each, 
    moving in opposite directions on an infinitely long straight road.
    """
    total_collisions = n * n
    return total_collisions