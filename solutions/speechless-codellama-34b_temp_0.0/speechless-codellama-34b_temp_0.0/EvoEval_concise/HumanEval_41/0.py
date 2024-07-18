

def car_race_collision(n: int) -> int:
    """
    On an infinitely long straight road, n cars are driving from left to right, while another n cars are driving from right to left at the same speed. A collision occurs when a car moving in one direction hits a car moving in the opposite direction. Despite collisions, all cars keep moving in their original direction. The function returns the total number of such collisions.
    """
    return n * (n - 1) // 2