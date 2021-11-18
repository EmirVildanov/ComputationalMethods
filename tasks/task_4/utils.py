from typing import Callable

import numpy as np
import sympy

from tasks.utils.calculation import get_function, find_absolute_discrepancy_value

weight_function_expression, weight_function_lambda = get_function("1")
x_symbol = sympy.Symbol('x')


def float64(number) -> np.float64:
    return np.float64(number)


def find_h(a: np.float64, b: np.float64, m: int) -> np.float64:
    return float64((b - a) / m)


def integral_of_function_multiplication():
    function_expression, function_lambda = get_function("")
    whole = f"({function_expression}) * ({function_expression})".replace("e", "E")
    result = sympy.sympify(whole)
    integral = result.integrate((x_symbol, 0, 1))
    print(f"Integral: {integral}")


def print_method_info(J, actual, theoretical_discrepancy):
    print(f"Value: {actual}")
    actual_absolute_discrepancy = find_absolute_discrepancy_value(J, actual)
    print(f"Absolute values of discrepancy: {actual_absolute_discrepancy}")
    print(f"Theoretical discrepancy: {theoretical_discrepancy}")
    print(
        f"Discrepancies' diff: {find_absolute_discrepancy_value(actual_absolute_discrepancy, theoretical_discrepancy)}")


class Method:
    def __init__(self, method: Callable, name):
        self.method = method
        self.name = name
