
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    last_seen = lst[0]
    current_count = 1
    for i in range(1, len(lst)):
        if lst[i] < last_seen:
            return False
        elif lst[i] == last_seen:
            current_count += 1
            if current_count > 2:
                return False
        else:
            current_count = 1
            last_seen = lst[i]
    return True