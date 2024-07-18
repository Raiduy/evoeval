def magicTrick(cards, magicNumber):
    """
    In this problem, you are a magician who needs to perform a card trick. You have a list of cards, each marked with a number, and a magic number.

    Your task is to implement a function that takes a list of card numbers and a magic number. The function should determine whether it's possible to select two cards such that when multiplied, their product equals the magic number.

    The function should return the indices of the two cards if it's possible, and "No magic today" if it's not. The indices should be 0-indexed and returned in an ascending order i.e., (smaller index, larger index). 

    For example:
    magicTrick([2, 3, 4, 5], 20) => (2, 3)
    magicTrick([1, 1, 1, 1], 1) => (0, 1)
    magicTrick([1, 2, 3, 4], 10) => "No magic today"

    It is assumed that the input list will be non-empty and the magic number will be a positive integer.
    """
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            if cards[i] * cards[j] == magicNumber:
                return (i, j)
    return 'No magic today'