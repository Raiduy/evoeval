import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Initial guess
    x = 0.0
    # Tolerance
    epsilon = 1e-7
    # Maximum number of iterations
    max_iterations = 1000
    for _ in range(max_iterations):
        fx = poly(xs, x)
        if abs(fx) < epsilon:
            return x
        dfx = poly_derivative(xs, x)
        if dfx == 0:
            raise ValueError("Derivative is zero. The Newton-Raphson method fails.")
        x = x - fx / dfx
    raise ValueError("The Newton-Raphson method did not converge.")
