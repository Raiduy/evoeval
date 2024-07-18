
def choose_num(x, y):
    # If y is less than x, then we return -1
    if y < x:
        return -1
    # If y is not less than x, then we find the biggest even number in the range [x, y]
    else:
        # We start from y and decrease the number until we find the biggest even number
        for i in range(y, x-1, -1):
            # If i is even then we return i
            if i % 2 == 0:
                return i
        # If there's no even number in the range [x, y] then we return -1
        return -1
