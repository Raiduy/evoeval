def galactic_travel(t, v):
    """Given the time (t) in years and average velocity (v) in km/s, calculate the distance traveled in light years in a galaxy far, far away.
    Assume that 1 light year is approximately 9.461 x 10^12 km.

    >>> galactic_travel(1, 300000)
    0.9999788605855617
    """
    distance_km = t * v * 3600 * 24 * 365.25
    distance_ly = distance_km / 9461000000000.0
    return distance_ly