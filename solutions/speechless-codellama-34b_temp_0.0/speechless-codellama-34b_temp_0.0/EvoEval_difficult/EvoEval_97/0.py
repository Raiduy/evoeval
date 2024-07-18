def multiplyComplex(a, b):
    (real_a, imag_a) = map(int, a.split('+')[0].split('-'))
    (real_b, imag_b) = map(int, b.split('+')[0].split('-'))
    real_product = real_a * real_b - imag_a * imag_b
    imag_product = real_a * imag_b + real_b * imag_a
    return {'real': real_product, 'imaginary': imag_product}