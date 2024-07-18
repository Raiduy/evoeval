import math

def max_fill(grid, capacity):
    # Initialize the count of buckets
    bucket_count = 0

    # Iterate over each row in the grid
    for row in grid:
        # Calculate the sum of the row
        row_sum = sum(row)

        # If the row sum is greater than the capacity
        if row_sum > capacity:
            # Increase the bucket count by the row sum divided by the capacity, rounded up
            bucket_count += math.ceil(row_sum / capacity)
        elif row_sum > 0:
            # If the row sum is less than the capacity and greater than 0, increase the bucket count by 1
            bucket_count += 1

    # Return the bucket count
    return bucket_count
