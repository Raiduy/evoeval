from typing import List

def magical_alphabet(input_string: str) -> List[str]:
    """ 
    Given a string where 'a' represents '1', 'b' represents '2', 'c' represents '3' ... 'z' represents '26'. 
    This function should return a list of all possible combinations based on the interpretation of the input string. 
    For example, if input is '123', it should return ['abc', 'lc', 'aw'] which represents ['1,2,3', '12,3', '1,23'].

    >>> magical_alphabet('123')
    ['abc', 'lc', 'aw']
    
    >>> magical_alphabet('111')
    ['aaa', 'ak', 'ka']
    
    Note: Assume all input strings will only contain digits
    """

    def helper(data, k, result):
        if k == 0:
            result.append(data)
        else:
            first = k[0]
            if first != '0':
                helper(data + chr(int(first) + 96), k[1:], result)
            if len(k) > 1:
                second = k[1]
                if first != '0' and int(first + second) <= 26:
                    helper(data + chr(int(first + second) + 96), k[2:], result)
    result = []
    helper('', input_string, result)
    return result