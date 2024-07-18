
def fruit_distribution(s, n):
    # extract numbers from the string using regex
    numbers = [int(i) for i in s.split() if i.isdigit()]
    
    # extract the number of apples and oranges
    apples = numbers[0]
    oranges = numbers[1]
    
    # calculate the number of mango fruits
    mango = n - apples - oranges
    
    return mango
