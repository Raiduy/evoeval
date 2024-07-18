
def is_sorted(lst):
    # Check if the list is sorted in ascending order
    if lst != sorted(lst):
        return False
    
    # Check for more than one duplicate of the same number
    for num in lst:
        if lst.count(num) > 2:
            return False
    
    return True
