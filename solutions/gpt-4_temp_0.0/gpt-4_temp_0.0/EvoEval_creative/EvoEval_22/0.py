def galactic_travel(t, v):
    """Given the time (t) in years and average velocity (v) in km/s, calculate the distance traveled in light years in a galaxy far, far away.
    Assume that 1 light year is approximately 9.461 x 10^12 km.

    >>> galactic_travel(1, 300000)
    0.9999788605855617
    """
    v_year = v * 60 * 60 * 24 * 365
    d_km = v_year * t
    d_ly = d_km / (9.461 * 10 ** 12)
    return d_ly