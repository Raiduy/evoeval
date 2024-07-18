def create_pyramid(p):
    """
    Given a positive integer p, your objective is to construct a pyramid. The base of the pyramid has p blocks. 
    The number of blocks in the next layer depends upon whether the number of blocks in the previous layer is even or odd.
    The rules are as follows:
        - If the number of blocks in the previous layer is even, the next layer contains 2 blocks less.
        - If the number of blocks in the previous layer is odd, the next layer contains 3 blocks less.
    Before the number of blocks in the next layer is less than or equal to zero, the pyramid is complete. Your function should return 
    a list containing the number of blocks in each layer from bottom to top. The element at index i in the list represents 
    the number of blocks in the (i+1)th layer from the bottom. 

    Examples:
    >>> create_pyramid(10)
    [10, 8, 6, 4, 2]
    
    >>> create_pyramid(9)
    [9, 6, 4, 2]
    """
    pyramid = []
    while p > 0:
        pyramid.append(p)
        if p % 2 == 0:
            p -= 2
        else:
            p -= 3
    return pyramid