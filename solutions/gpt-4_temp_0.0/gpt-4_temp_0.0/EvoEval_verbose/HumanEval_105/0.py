
def by_length(arr):
    num_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    filtered_arr = [num for num in arr if num in num_to_word.keys()]
    sorted_arr = sorted(filtered_arr, reverse=True)
    result = [num_to_word[num] for num in sorted_arr]
    return result