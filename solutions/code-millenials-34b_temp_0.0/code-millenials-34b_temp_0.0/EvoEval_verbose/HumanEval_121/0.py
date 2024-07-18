
def solution(lst):
    return sum((value for (index, value) in enumerate(lst) if index % 2 == 0 and value % 2 != 0))