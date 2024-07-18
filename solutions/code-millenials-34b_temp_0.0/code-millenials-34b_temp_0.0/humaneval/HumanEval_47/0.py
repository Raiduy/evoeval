

def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    s = sorted(l)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n%2] if n else None
