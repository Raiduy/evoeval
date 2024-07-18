
def by_length(arr):
    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    filtered_arr = [i for i in arr if 1 <= i <= 9]
    filtered_arr.sort()
    filtered_arr = filtered_arr[::-1]
    result = [num2words[i] for i in filtered_arr]
    return result