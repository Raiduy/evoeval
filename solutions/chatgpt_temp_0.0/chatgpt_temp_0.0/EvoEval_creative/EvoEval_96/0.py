def get_magic_indices(lst):

    def product_of_digits(num):
        product = 1
        for digit in str(abs(num)):
            product *= int(digit)
        return product
    magic_indices = []
    for (i, num) in enumerate(lst):
        if i != 0 and num % i == 0 and (product_of_digits(num) == i):
            magic_indices.append(i)
    return sorted(magic_indices)