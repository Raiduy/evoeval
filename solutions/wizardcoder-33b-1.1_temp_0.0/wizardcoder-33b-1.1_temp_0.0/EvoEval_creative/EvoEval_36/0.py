def calculate_integral_coefficients(xs: list):
    integral_coefficients = [0] * (len(xs) + 1)
    for i in range(len(xs)):
        integral_coefficients[i + 1] = xs[i] / (i + 1)
    return integral_coefficients