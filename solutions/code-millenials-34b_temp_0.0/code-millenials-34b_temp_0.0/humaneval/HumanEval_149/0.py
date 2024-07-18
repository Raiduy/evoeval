
def sorted_list_sum(lst):
    # Delete the strings that have odd lengths
    lst = [s for s in lst if len(s) % 2 == 0]

    # Return the resulted list with a sorted order
    return sorted(lst, key=lambda x: (len(x), x))
