
def by_length(arr):
    arr = [i for i in arr if 1 <= i <= 9]
    arr.sort()
    arr.reverse()
    num_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    arr = [num_to_word[i] for i in arr]
    return arr