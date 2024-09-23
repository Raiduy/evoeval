def fairy_tale_transport(q, w, e):
    """
    In a fairy tale world, three types of magical creatures are there: unicorns, dragons, and griffins. The unicorns can carry 'w' kg, dragons can carry 'e' kg, and griffins can carry 'e' kg of weight. You have a list of weights of different items you want to carry.
    
    Write a function that returns True if the combined strength of these magical creatures can carry all the items, and False otherwise. 

    The function will take three parameters - a list q of weights of items, an integer w representing the carrying capacity of unicorns, an integer e representing the carrying capacity of dragons and griffins together.
    
    Example:
    fairy_tale_transport([5, 10, 15], 5, 20) ➞ False
    
    fairy_tale_transport([10, 20, 30], 5, 10) ➞ False

    fairy_tale_transport([1, 2, 3], 1, 5) ➞ True
    
    fairy_tale_transport([5, 10, 15], 15, 15) ➞ True
    """
    total_weight = sum(q)
    total_capacity = w + e
    if total_weight <= total_capacity:
        return True
    else:
        return False