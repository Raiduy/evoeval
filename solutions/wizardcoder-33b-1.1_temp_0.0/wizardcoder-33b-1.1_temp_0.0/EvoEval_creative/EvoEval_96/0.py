def get_magic_indices(lst):

    def product_of_digits(n):
        n = abs(n)
        product = 1
        while n > 0:
            product *= n % 10
            n //= 10
        return product
    magic_indices = []
    for (i, val) in enumerate(lst):
        if val % i == 0 and product_of_digits(val) == i:
            magic_indices.append(i)
    return magic_indices