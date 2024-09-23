def multiplyComplex(a, b):
    (a_real, a_imag) = map(int, a.replace('i', '').split('+') if '+' in a else map(int, a.replace('i', '').split('-')))
    (b_real, b_imag) = map(int, b.replace('i', '').split('+') if '+' in b else map(int, b.replace('i', '').split('-')))
    if '-' in a:
        a_imag *= -1
    if '-' in b:
        b_imag *= -1
    real = a_real * b_real - a_imag * b_imag
    imaginary = a_real * b_imag + a_imag * b_real
    return {'real': real, 'imaginary': imaginary}