def galactic_travel(t, v):
    """Given the time (t) in years and average velocity (v) in km/s, calculate the distance traveled in light years in a galaxy far, far away.
    Assume that 1 light year is approximately 9.461 x 10^12 km.

    >>> galactic_travel(1, 300000)
    0.9999788605855617
    """
    t_seconds = t * 365 * 24 * 60 * 60
    light_year_distance = v * t_seconds / (9.461 * 10 ** 12)
    return light_year_distance