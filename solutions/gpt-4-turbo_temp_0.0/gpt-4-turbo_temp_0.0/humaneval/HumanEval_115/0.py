import math

def max_fill(grid, capacity):
    # Count the total number of units of water in the grid
    total_water_units = sum(row.count(1) for row in grid)
    
    # Calculate the number of times buckets need to be lowered
    # We use math.ceil to round up since any remaining water requires a full bucket dip
    bucket_dips = math.ceil(total_water_units / capacity)
    
    return bucket_dips
