import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """
    Finds a zero of the polynomial with coefficients xs.
    Assumes there is at least one real root.
    """
    # Define an initial search interval
    left, right = -1000, 1000
    while left <= right:
        mid = (left + right) / 2
        val = poly(xs, mid)
        
        # Check if mid is close enough to be considered a root
        if abs(val) < 1e-6:
            return mid
        elif val > 0:
            right = mid
        else:
            left = mid

    # Fallback in case the loop exits without finding a root
    # This should not happen with the assumptions given
    raise ValueError("Root not found within the search interval.")
