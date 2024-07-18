
def by_length(arr):
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr, reverse=True)
    english_words = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [english_words[num - 1] for num in sorted_arr]
    return result