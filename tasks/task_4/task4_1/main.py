import random
from typing import Callable, List

from tasks.task_4.task_4_constants import *
from tasks.utils.calculation import find_absolute_discrepancy_value
from tasks.utils.handsome_printer import print_red, print_green


def print_task_info():
    # Приближённое вычисление интеграла по квадратурным формулам
    print("Theme: Approximate calculation of the integral by quadrature formulas")
    print()


def left_rectangle_method(function, a, b):
    return (b - a) * function(a)


def right_rectangle_method(function, a, b):
    return (b - a) * function(b)


def middle_rectangle_method(function, a, b):
    return (b - a) * function((a + b) / 2.0)


def trapezoid_method(function, a, b):
    return ((b - a) / 2) * (function(a) + function(b))


def simpsons_method(function, a, b):
    return ((b - a) / 6) * (function(a) + 4 * function((a + b) / 2) + function(b))


def three_eights_method(function, a, b):
    h = (b - a) / 3
    return (b - a) * (
            (1 / 8) * function(a) + (3 / 8) * function(a + h) +
            (3 / 8) * function(a + 2 * h) + (1 / 8) * function(b)
    )


def print_method_info(J, actual):
    print(f"Value: {actual}")
    print(f"Absolute values of discrepancy: {find_absolute_discrepancy_value(J, actual)}")


class Method:
    def __init__(self, method: Callable[[Callable, float, float], None], name):
        self.method = method
        self.name = name


def test_polynomial(polynomial: Polynomial, methods: List[Method]) -> bool:
    epsilon = pow(10, -20)
    # a = random.uniform(-100, 100)
    # b = random.uniform(-100, 100)
    # while b < a:
    #     b = random.uniform(-100, 100)
    a = 0
    b = 1
    expected = polynomial.integral(b) - polynomial.integral(a)
    for method in methods:
        current_actual = method.method(polynomial.polynomial_lambda, a, b)
        discrepancy = find_absolute_discrepancy_value(current_actual, expected)
        if discrepancy > epsilon:
            print_red(f"Test failed on {method.name}. Discrepancy = {discrepancy} ")
            return False
    print_green(f"Test passed")
    return True


if __name__ == "__main__":
    print_task_info()

    user_input = ""
    while user_input.strip() != "exit":
        # a = float(input("Enter a: "))
        # b = float(input("Enter b: "))
        a = -10
        b = 13

        # the grater (b - a) the greater the value of absolute discrepancy

        while b <= a:
            b = int(input("b must be greater than a. Try again: "))

        J = integral_for_easily_integrated_function(a, b)
        print(f"Exact value of easily integrated function from a to b: {J}")

        methods = [
            Method(left_rectangle_method, "Left rectangle method"),
            Method(right_rectangle_method, "Right rectangle method"),
            Method(middle_rectangle_method, "Middle rectangle method"),
            Method(trapezoid_method, "Trapezoid method"),
            Method(simpsons_method, "Simpson method"),
            Method(three_eights_method, "Three eights method")
        ]

        print("Approximated values of easily integrated function from a to b:")
        for method in methods:
            print_red(f"-------{method.name}-------")
            value = method.method(easily_integrated_function, a, b)
            print_method_info(J, value)
        print()

        methods_with_0_degree_of_accuracy = methods
        methods_with_1_degree_of_accuracy = methods[2:]
        methods_with_3_degree_of_accuracy = methods[4:]

        print("Tests on polynomials:")

        test_polynomial(polinomial_of_0_degree, methods_with_0_degree_of_accuracy)
        test_polynomial(polinomial_of_1_degree, methods_with_1_degree_of_accuracy)
        test_polynomial(polinomial_of_2_degree, methods_with_3_degree_of_accuracy)
        test_polynomial(polinomial_of_3_degree, methods_with_3_degree_of_accuracy)
        print()

        a = float(1.13456789012345678)
        print(a)
        user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")
