def fruit_distribution(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket minus one return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples, 6 oranges", 19) ->19 +1  - 5 - 6 = 9
    fruit_distribution("0 apples, 1 oranges",3) -> 3 + 1 - 0 - 1 = 3
    fruit_distribution("2 apples, 3 oranges", 100) -> 100 + 1- 2 - 3 = 96
    fruit_distribution("100 apples, 1 oranges",120) -> 120 + 1- 100 - 1 = 20
    """
    words = s.split()
    apples = int(words[0])
    oranges = int(words[2])
    mangoes = n - apples - oranges - 1
    return mangoes