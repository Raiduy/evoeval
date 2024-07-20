
def get_max_triples(n):
    """
    Given a positive integer n, create an array a of length n where each element a[i] = i * i - i + 1.
    Return the count of triples (a[i], a[j], a[k]) where i < j < k and the sum of the triples is divisible by 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        Only triple whose sum is divisible by 3 is (1, 7, 13).
    """
    a = [i * i - i + 1 for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count