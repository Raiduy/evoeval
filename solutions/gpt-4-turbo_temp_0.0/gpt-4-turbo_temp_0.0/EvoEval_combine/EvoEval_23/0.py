
def special_stone_factorial(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones. The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.

    For each level, calculate the Brazilian factorial (defined as: brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!), 
    where n is the number of stones in the level.

    Return the list of Brazilian factorials for each level.
    """
    brazilian_factorials = []
    current_stone_count = n
    for _ in range(n):
        brazilian_factorials.append(brazilian_factorial(current_stone_count))
        if current_stone_count % 2 == 0:
            current_stone_count += 1
        else:
            current_stone_count += 2
    return brazilian_factorials