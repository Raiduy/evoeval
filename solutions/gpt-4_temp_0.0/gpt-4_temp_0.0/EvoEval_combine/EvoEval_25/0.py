
from typing import List, Tuple

def sum_product_triples(n: int) -> Tuple[int, int]:
    """
    You are given a positive integer n. You have to create an integer array a of length n.
    For each i (from 1 to n), the value of a[i] = i * i - i + 1.
    Find the triples (a[i], a[j], a[k]) of a where i < j < k, and a[i] + a[j] + a[k] is a multiple of 3.
    From these triples, return a tuple consisting of the sum and the product of all the first elements of these triples.
    
    Empty sum should be equal to 0 and empty product should be equal to 1 if there are no valid triples.
    
    Example :
        Input: n = 5
        Output: (1, 1)
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13). The sum and product of the first element is 1. 
    """
    a = [i * i - i + 1 for i in range(1, n + 1)]
    sum_val = 0
    product_val = 1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    sum_val += a[i]
                    product_val *= a[i]
    if sum_val == 0:
        product_val = 1
    return (sum_val, product_val)