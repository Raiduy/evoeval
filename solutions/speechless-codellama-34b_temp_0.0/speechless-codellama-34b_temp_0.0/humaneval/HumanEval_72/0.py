
def will_it_fly(q, w):
    # Check if the list is a palindrome
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal to w
        if sum(q) <= w:
            return True
    return False
