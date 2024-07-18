
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots that exist in stock
    """
    # Calculate how many carrots you can eat based on your need and the remaining carrots.
    carrots_eaten = min(need, remaining)
    
    # Update the total number of eaten carrots.
    total_eaten = number + carrots_eaten
    
    # Calculate the number of carrots left after eating.
    carrots_left = remaining - carrots_eaten
    
    return [total_eaten, carrots_left]
