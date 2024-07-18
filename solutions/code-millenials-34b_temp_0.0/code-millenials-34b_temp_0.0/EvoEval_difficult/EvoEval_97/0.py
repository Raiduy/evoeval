def multiplyComplex(a, b):
    (a_real, a_imaginary) = map(int, a.split('+')[0].split('-'))
    (b_real, b_imaginary) = map(int, b.split('+')[0].split('-'))
    real = a_real * b_real - a_imaginary * b_imaginary
    imaginary = a_real * b_imaginary + a_imaginary * b_real
    return {'real': real, 'imaginary': imaginary}