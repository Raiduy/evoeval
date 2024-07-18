
def get_max_triples(n):
    # Generate the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Count the number of elements in a that are 0, 1, and 2 modulo 3
    mod_counts = [0, 0, 0]
    for value in a:
        mod_counts[value % 3] += 1
    
    # Calculate the number of valid triples
    # A valid triple can be formed by choosing 3 elements that are all 0 modulo 3,
    # or by choosing one element from each residue class modulo 3.
    valid_triples = mod_counts[0] * (mod_counts[0] - 1) * (mod_counts[0] - 2) // 6  # Combination of 3 elements all 0 mod 3
    valid_triples += mod_counts[0] * (mod_counts[1]) * (mod_counts[2])  # One element from each residue class
    valid_triples += mod_counts[1] * (mod_counts[1] - 1) * (mod_counts[1] - 2) // 6  # Combination of 3 elements all 1 mod 3
    valid_triples += mod_counts[2] * (mod_counts[2] - 1) * (mod_counts[2] - 2) // 6  # Combination of 3 elements all 2 mod 3
    
    return valid_triples
