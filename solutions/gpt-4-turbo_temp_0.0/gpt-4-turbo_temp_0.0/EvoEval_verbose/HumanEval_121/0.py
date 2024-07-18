
def solution(lst):
    sum_odd_even_pos = 0
    for (index, value) in enumerate(lst):
        if index % 2 == 0 and value % 2 != 0:
            sum_odd_even_pos += value
    return sum_odd_even_pos