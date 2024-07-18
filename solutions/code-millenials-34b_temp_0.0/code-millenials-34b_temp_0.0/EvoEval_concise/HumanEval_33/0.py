

def sort_third(l: list):
    sorted_indices = sorted(range(len(l)), key=lambda i: l[i] if i % 3 == 0 else -1)
    return [l[i] for i in sorted_indices]