def car_race_collision(n: int, speeds: list):
    left_to_right_cars = [i for i in range(n)]
    right_to_left_cars = [i for i in range(n)]
    collisions = 0
    for i in range(n):
        for j in range(n):
            if speeds[i] == 0 or speeds[j] == 0:
                collisions += 1
            elif speeds[i] > speeds[j]:
                collisions += 1
    return collisions