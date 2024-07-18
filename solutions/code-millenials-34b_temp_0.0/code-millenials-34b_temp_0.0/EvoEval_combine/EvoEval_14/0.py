
def prime_avg_range(n, m):
    if n > m:
        return -1
    prime_numbers = [i for i in range(n, m + 1) if is_prime(i)]
    if not prime_numbers:
        return -1
    avg = round(sum(prime_numbers) / len(prime_numbers))
    return bin(avg)