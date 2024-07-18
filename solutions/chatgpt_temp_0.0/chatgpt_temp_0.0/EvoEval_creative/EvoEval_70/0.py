def planet_path(planets, path):
    """Given a dictionary of planets where each planet is a key and its value is 
    a list of planets it directly connects to, and a list of planets forming a path, 
    return True if the path between those planets is valid (i.e. each planet connects 
    directly to the next), and False otherwise. If the planet does not exist in the 
    dictionary or the path list is empty, return False.

    Example:
    planet_path({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}, ['a', 'b', 'c']) 
    returns True
    planet_path({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}, ['a', 'c', 'b']) 
    returns True
    planet_path({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}, ['a', 'b', 'a']) 
    returns True
    planet_path({'a': ['b'], 'b': ['a', 'c'], 'c': ['b']}, ['a', 'c', 'b']) 
    returns False
    planet_path({'a': ['b'], 'b': ['a', 'c'], 'c': ['b']}, []) 
    returns False
    planet_path({}, ['a', 'b', 'c']) 
    returns False
    """
    if not path or not planets:
        return False
    for i in range(len(path) - 1):
        current_planet = path[i]
        next_planet = path[i + 1]
        if current_planet not in planets or next_planet not in planets[current_planet]:
            return False
    return True