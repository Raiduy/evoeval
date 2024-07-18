

def monotonic(l: list):
    """Checks if list elements are monotonically increasing or decreasing."""
    return all((l[i] <= l[i + 1] for i in range(len(l) - 1))) or all((l[i] >= l[i + 1] for i in range(len(l) - 1)))