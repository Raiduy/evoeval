

def below_threshold(l: list, t: int):
    """
    This function takes in two arguments: a list of integers 'l' and an integer 't', which is referred to as the threshold. 
    The function's main purpose is to check whether all the integers in the list 'l' are less than the threshold 't'.
    
    If all the integers in 'l' are indeed less than 't', the function will return True. 
    However, if there is at least one integer in 'l' that is not less than 't', it will return False.
    
    This is shown in the examples below:
    
    If called with a list [1, 2, 4, 10] and a threshold of 100, the function below_threshold([1, 2, 4, 10], 100) will return True, 
    because all numbers in the list are below the threshold of 100.
    
    But if the function is called with a list [1, 20, 4, 10] and a threshold of 5, the function below_threshold([1, 20, 4, 10], 5) 
    will return False, because the number 20 in the list is not below the threshold of 5.
    """
    for i in l:
        if i >= t:
            return False
    return True