

def car_race_collision(n: int):
    """
    Consider a scenario where there is a road that extends infinitely in a straight line in both directions.
    On this road, there are 'n' cars that are driving from the left to the right direction. At the same time, 
    there is another group of 'n' cars that are driving from the right to the left direction. Initially, these 
    two groups of cars are located far apart from one another. All cars in both groups are moving at the same 
    speed, regardless of their direction.

    A collision between two cars is defined as an event where a car moving from the left to the right comes 
    into contact with a car moving from the right to the left. Despite these collisions, all cars involved 
    continue moving in their original direction without any changes to their speed or trajectory. This is 
    because all cars are considered to be infinitely sturdy and strong, allowing them to withstand any 
    collisions without being affected.

    The function 'car_race_collision' is expected to calculate and return the total number of such collisions 
    that occur between these two groups of cars. The input to the function is the number of cars 'n' in each 
    group and the output will be the total number of collisions that occur as these cars pass each other on 
    the road.
    """
    total_collisions = n * 2
    return total_collisions