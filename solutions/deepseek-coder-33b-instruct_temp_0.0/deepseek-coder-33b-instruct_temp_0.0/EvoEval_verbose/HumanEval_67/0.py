
def fruit_distribution(s, n):
    """
    This function, fruit_distribution, is designed to calculate the number of a specific type of fruit, in this case mangoes, within a mixed fruit basket. The basket contains three different types of fruits: apples, oranges, and mangoes. 

    The  function requires two inputs. The first input, 's', is a string that represents the total number of oranges and apples in the basket. The format of this string should be a combination of two integers and two fruit names (apples and oranges) such as "5 apples and 6 oranges".

    The second input, 'n', is an integer that represents the total number of fruits in the basket. This number includes all types of fruits: apples, oranges, and mangoes.

    The function works by subtracting the number of apples and oranges (extracted from the string 's') from the total number of fruits in the basket (the integer 'n'). The resultant value is the number of mangoes in the basket.

    Here are a few examples to illustrate how the function works:

    Example 1:
    fruit_distribution("5 apples and 6 oranges", 19) 
    The function will subtract the sum of apples and oranges (5+6=11) from the total number of fruits (19). 
    So, the result is 19 - 11 = 8. Hence, there are 8 mangoes in the basket.

    Example 2:
    fruit_distribution("0 apples and 1 oranges",3) 
    The function will subtract the sum of apples and oranges (0+1=1) from the total number of fruits (3). 
    So, the result is 3 - 1 = 2. Hence, there are 2 mangoes in the basket.

    Example 3:
    fruit_distribution("2 apples and 3 oranges", 100) 
    The function will subtract the sum of apples and oranges (2+3=5) from the total number of fruits (100). 
    So, the result is 100 - 5 = 95. Hence, there are 95 mangoes in the basket.

    Example 4:
    fruit_distribution("100 apples and 1 oranges",120) 
    The function will subtract the sum of apples and oranges (100+1=101) from the total number of fruits (120). 
    So, the result is 120 - 101 = 19. Hence, there are 19 mangoes in the basket.
    """
    words = s.split()
    apples = int(words[0])
    oranges = int(words[2])
    mangoes = n - (apples + oranges)
    return mangoes