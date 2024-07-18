
def max_fill(grid, capacity):
    import math
    num_lowerings = 0
    for row in grid:
        for well in row:
            water_units = sum(well)
            well_lowerings = math.ceil(water_units / capacity)
            num_lowerings += well_lowerings
    return num_lowerings