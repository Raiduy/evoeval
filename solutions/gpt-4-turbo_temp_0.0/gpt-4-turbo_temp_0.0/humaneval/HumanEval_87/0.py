
def get_row(lst, x):
    """
    Given a 2D list `lst` and an integer `x`, find all occurrences of `x` in the list,
    and return a list of tuples representing their coordinates, sorted by row in ascending
    order and by column in descending order within each row.
    """
    # Initialize an empty list to store the coordinates
    coordinates = []
    
    # Iterate through each row and column to find occurrences of `x`
    for row_idx, row in enumerate(lst):
        for col_idx, value in enumerate(row):
            if value == x:
                # If the current element is `x`, add its coordinates to the list
                coordinates.append((row_idx, col_idx))
    
    # Sort the coordinates by row in ascending order and by column in descending order
    # This is achieved by sorting by row first, then by column in reverse
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))
    
    return coordinates
