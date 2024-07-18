
def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]
    count = 0
    remainders = [0, 0, 0]
    
    for x in a:
        remainders[x % 3] += 1
        
    count += remainders[0] * (remainders[0] - 1) * (remainders[0] - 2) // 6
    count += remainders[1] * remainders[2] * 3
    count += remainders[0] * remainders[1] * 3
    
    return count
