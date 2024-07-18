def calculate_integral_coefficients(xs: list):
    integral_coefficients = [0.0]
    for i in range(len(xs)):
        integral_coefficients.append(xs[i] / (i + 1))
    return integral_coefficients