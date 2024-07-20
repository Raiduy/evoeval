
from typing import List

def sort_parentheses(lst: List[str]) -> str:
    """
    You are given a list of strings, each string consist of open parentheses '(' or close parentheses ')' 
    and numberals from 'zero' to 'nine' in text form.
    Your job is to sort the numbers from smallest to largest and then check if it is possible to concatenate 
    the strings in this order so that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S are balanced. 
    For example: the string '(three)(one)(five)' is good, while the string '(three)(one(five)' is not.
    Return 'Yes' if there's a way to make a good string after sorting, and return 'No' otherwise.

    Examples:
    sort_parentheses(['(three)(', '(five)', '(one)']) == 'No'
    sort_parentheses(['(five)', '(three)', '(one)']) == 'Yes'
    """
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    sorted_lst = sorted(lst, key=lambda x: num_dict[x.strip('()')])
    sorted_str = ''.join(sorted_lst)
    open_count = 0
    for char in sorted_str:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count == 0:
                return 'No'
            open_count -= 1
    return 'Yes' if open_count == 0 else 'No'