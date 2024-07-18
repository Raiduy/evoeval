import math

def max_fill(grid, capacity):
    # Initialize the count of buckets used
    bucket_count = 0

    # Iterate over each row in the grid
    for row in grid:
        # Count the number of 1s in the row
        ones_count = row.count(1)

        # If the number of 1s is greater than the bucket capacity
        if ones_count > capacity:
            # Calculate the number of times the bucket needs to be lowered
            # by dividing the number of 1s by the bucket capacity and rounding up
            # to the nearest integer
            bucket_count += math.ceil(ones_count / capacity)
        elif ones_count > 0:
            # If the number of 1s is less than or equal to the bucket capacity,
            # only one bucket is needed
            bucket_count += 1

    # Return the total number of buckets used
    return bucket_count
