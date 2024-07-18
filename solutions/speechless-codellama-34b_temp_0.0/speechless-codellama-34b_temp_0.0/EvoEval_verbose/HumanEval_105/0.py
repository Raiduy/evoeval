
def by_length(arr):
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    word_arr = []
    for num in reversed_arr:
        if num == 1:
            word_arr.append('One')
        elif num == 2:
            word_arr.append('Two')
        elif num == 3:
            word_arr.append('Three')
        elif num == 4:
            word_arr.append('Four')
        elif num == 5:
            word_arr.append('Five')
        elif num == 6:
            word_arr.append('Six')
        elif num == 7:
            word_arr.append('Seven')
        elif num == 8:
            word_arr.append('Eight')
        elif num == 9:
            word_arr.append('Nine')
    return word_arr