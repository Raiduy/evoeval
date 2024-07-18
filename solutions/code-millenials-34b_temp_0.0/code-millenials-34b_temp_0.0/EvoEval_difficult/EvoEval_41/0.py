def car_race_collision(n: int, speeds: list):
    count = 0
    for speed in speeds:
        if speed <= 0:
            count += 1
    return count