def multiplyComplex(a, b):
    """Complete the function that takes two complex numbers as strings (in the form "a+bi" or "a-bi", where a & b are integers)
    and returns the product of the real and imaginary parts.
    Assume the input is always valid.
    Also, return the result as a dictionary with the keys as 'real' and 'imaginary'.
    """
    (a_real, a_imag) = map(int, a.replace('i', '').split('+') if '+' in a else a.replace('i', '').split('-'))
    (b_real, b_imag) = map(int, b.replace('i', '').split('+') if '+' in b else b.replace('i', '').split('-'))
    if '-' in a:
        a_imag = -a_imag
    if '-' in b:
        b_imag = -b_imag
    real_part = a_real * b_real - a_imag * b_imag
    imaginary_part = a_real * b_imag + a_imag * b_real
    return {'real': real_part, 'imaginary': imaginary_part}