from math import sin, log, cos


def find_h(n: int, A, B):
    if n < 2:
        raise RuntimeError(f"Broken N argument: {n}. It should be greater than 1")
    return (B - A) / n


def equation_function(x):
    return pow(2, -x) - sin(x)


def first_equation_function_derivative(x):
    return -pow(2, -x) * log(2) - cos(x)


task_title = "Numerical methods for solving nonlinear equations"
A = -5
B = 10
N = pow(10, 3)
h = find_h(N, A, B)
epsilon = pow(10, -7)
equation_function_string_view = "2^(-x) - sin(x)"
