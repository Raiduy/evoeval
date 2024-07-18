def get_magic_indices(lst):

    def product_of_digits(n):
        """Returns the product of the digits of a number."""
        n = abs(n)
        product = 1
        while n:
            product *= n % 10
            n //= 10
        return product
    magic_indices = []
    for (i, value) in enumerate(lst):
        if i == 0 and value == 0:
            magic_indices.append(i)
        elif i != 0 and value % i == 0:
            if product_of_digits(value) == i:
                magic_indices.append(i)
    return magic_indices