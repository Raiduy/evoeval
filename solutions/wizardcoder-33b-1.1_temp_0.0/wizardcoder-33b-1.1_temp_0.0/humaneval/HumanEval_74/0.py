
def total_match(lst1, lst2):
    # Calculate the total number of chars in each list
    total1 = sum(len(s) for s in lst1)
    total2 = sum(len(s) for s in lst2)

    # Return the list with less total number of chars
    if total1 < total2:
        return lst1
    else:
        return lst2
