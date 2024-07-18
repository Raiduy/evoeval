def helper_get_coordinates(string):
    """
    The helper function to fetch the x and y coordinates from a given string representation.
    
    The string representation will be in the format: (x,y)
    
    Parameters: 
    string (str): The string representation of the coordinates.
    
    Returns: 
    tuple: A tuple containing two integer values representing x and y coordinates.
    
    Example: 
    helper_get_coordinates("(2,3)") -> (2,3)
    helper_get_coordinates("(5,6)") -> (5,6)
    """

    x, y = string.replace("(","").replace(")","").split(",")
    return int(x), int(y)
def calculate_distance(coordinates_str_1, coordinates_str_2):
    """
    In this task, you will be given two string that represents x and y coordinates in a 2D plane.
    You are required to calculate the euclidean distance between these two points.
    The string representation of the coordinates will be in the format: (x,y)
    
    For example:
    calculate_distance("(2,3)", "(5,6)") -> The euclidean distance is sqrt((5-2)^2 + (6-3)^2) = sqrt(9+9) = sqrt(18) = 4.2426 rounded to 4 decimal places
    calculate_distance("(1,1)", "(4,5)") -> The euclidean distance is sqrt((4-1)^2 + (5-1)^2) = sqrt(9+16) = sqrt(25) = 5.0000 rounded to 4 decimal places
    """
    (x1, y1) = helper_get_coordinates(coordinates_str_1)
    (x2, y2) = helper_get_coordinates(coordinates_str_2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 4)