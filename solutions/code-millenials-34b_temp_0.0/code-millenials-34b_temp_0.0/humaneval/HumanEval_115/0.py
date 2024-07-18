import math

def max_fill(grid, capacity):
    count = 0
    for row in grid:
        temp = 0
        for i in row:
            if i == 1:
                temp += 1
        count += temp // capacity
        if temp % capacity != 0:
            count += 1
    return count
