
def solve(N):
    """Given a positive integer N, return the total sum of its digits represented as a hexadecimal number.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "6".
        For N = 147, the sum of digits will be 12 the output should be "c".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of hexadecimal number
    """
    str_N = str(N)
    sum_digits = 0
    for digit in str_N:
        sum_digits += int(digit)
    hex_sum = hex(sum_digits)[2:]
    return hex_sum