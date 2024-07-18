

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    l.sort()  # Sort the list to use two-pointer technique
    n = len(l)
    for i in range(n-2):  # The last two elements are already part of the last triplet check
        # Avoid duplicates for the first element
        if i > 0 and l[i] == l[i-1]:
            continue
        left, right = i + 1, n - 1  # Set left and right pointers
        while left < right:
            total = l[i] + l[left] + l[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left
    return False
