def planet_path(planets, path):
    if not path or path[0] not in planets:
        return False
    for i in range(len(path) - 1):
        if path[i + 1] not in planets[path[i]]:
            return False
    return True