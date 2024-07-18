def multiplyComplex(a, b):
    (a_real, a_imag) = map(int, a[:-1].split('+' if '+' in a else '-'))
    (b_real, b_imag) = map(int, b[:-1].split('+' if '+' in b else '-'))
    real = a_real * b_real - a_imag * b_imag
    imaginary = a_real * b_imag + a_imag * b_real
    return {'real': real, 'imaginary': imaginary}