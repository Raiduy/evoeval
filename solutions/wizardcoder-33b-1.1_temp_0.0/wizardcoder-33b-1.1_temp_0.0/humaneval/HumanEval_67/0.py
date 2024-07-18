
def fruit_distribution(s,n):
    # split the string into a list of words
    words = s.split()
    # get the number of apples and oranges
    apples = int(words[0])
    oranges = int(words[2])
    # calculate the number of mango fruits
    mango = n - apples - oranges
    return mango
