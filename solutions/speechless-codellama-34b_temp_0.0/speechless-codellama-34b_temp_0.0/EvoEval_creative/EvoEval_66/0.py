def prime_anagram_pairs(n):
    prime_numbers = [i for i in range(2, n + 1) if is_prime(i)]
    anagram_pairs = []
    for i in range(len(prime_numbers)):
        for j in range(i + 1, len(prime_numbers)):
            if sorted(str(prime_numbers[i])) == sorted(str(prime_numbers[j])):
                anagram_pairs.append((prime_numbers[i], prime_numbers[j]))
    return sorted(anagram_pairs, key=lambda x: (x[0], x[1]))