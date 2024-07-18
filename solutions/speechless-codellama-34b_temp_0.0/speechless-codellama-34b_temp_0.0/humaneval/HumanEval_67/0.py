
def fruit_distribution(s,n):
    # Split the string into a list of words
    words = s.split()
    # Extract the number of apples and oranges from the list
    apples = int(words[0])
    oranges = int(words[3])
    # Calculate the number of mango fruits
    mango = n - apples - oranges
    return mango
