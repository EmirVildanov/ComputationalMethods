import random
from enum import Enum, auto
from typing import Tuple

import numpy as np
import sympy
from sympy import lambdify, solve

from tasks.task_4.task_4_constants import Polynomial, polinomial_of_0_degree, polinomial_of_1_degree, \
    polinomial_of_2_degree, polinomial_of_3_degree
from tasks.task_4.utils import float64, Method, x_symbol, weight_function_lambda, find_h, print_method_info
from tasks.utils.calculation import find_absolute_discrepancy_value, get_function
from tasks.utils.handsome_printer import print_red, print_green


def left_rectangle_method(function_lambda, weight_function_lambda, a: np.float64, h: np.float64, m: int) -> Tuple[np.float64, np.float64]:
    sum = 0
    alfa = a

    f_0 = function_lambda(alfa) * weight_function_lambda(alfa)

    for j in range(1, m):
        sum += function_lambda(alfa + j * h) * weight_function_lambda(alfa + j * h)
    result = h * (f_0 + sum)

    # sum = w
    return result, sum


def right_rectangle_method(function, weight_function, a: np.float64, h: np.float64, m: int, w: np.float64) -> np.float64:
    alfa = a + h

    return h * (w + function(alfa + m * h) * weight_function(alfa + m * h))


def middle_rectangle_method(function, weight_function, a: np.float64, h: np.float64, m: int) -> Tuple[np.float64, np.float64]:
    alfa = a + h / 2
    sum = 0

    for j in range(0, m):
        sum += function(alfa + j * h) * weight_function(alfa + j * h)
    result = h * sum

    # sum = q
    return result, sum


def trapezoid_method(function, weight_function, a: np.float64, h: np.float64, m: int, w: np.float64) -> \
        Tuple[np.float64, np.float64]:
    alfa = a
    f_0 = function(alfa) * weight_function(alfa)
    f_m = function(alfa + m * h) * weight_function(alfa + m * h)

    # f_0 + f_m = z
    return (h / 2) * (f_0 + f_m + 2 * w), f_0 + f_m


def simpsons_method(h: np.float64, z: np.float64, w: np.float64,
                    q: np.float64) -> np.float64:
    return (h / 6) * (z + 2 * w + 4 * q)


def find_absolute_maximum_on_segment(function, arg, a: np.float64, b: np.float64):
    class DotType(Enum):
        MAX = auto()
        MIN = auto()
        INFLECTION = auto()

    def get_dot_type(function, arg, val) -> DotType:
        def get_deep_dot_type(function, arg, val, n=3) -> DotType:
            dy = function.diff(arg)
            dyn = dy.subs(arg, val)
            if dyn == 0:
                return get_deep_dot_type(dy, arg, val, n + 1)
            elif n % 2 == 1:
                return DotType.INFLECTION
            elif dyn > 0:
                return DotType.MIN
            else:
                return DotType.MAX

        dy = function.subs(arg, val)
        if dy > 0:
            return DotType.MIN
        elif dy < 0:
            return DotType.MAX
        else:
            return get_deep_dot_type(function, arg, val)

    dy = function.diff(arg)
    ddy = dy.diff(arg)
    extremes = solve(dy, arg)
    absolute_maximum_pretenders = []

    for extreme in extremes:
        dotType = get_dot_type(ddy, arg, extreme)
        if dotType is DotType.MAX:
            absolute_maximum_pretenders.append(extreme)
    absolute_maximum_pretenders.append(a)
    absolute_maximum_pretenders.append(b)

    lambda_f = lambdify("x", function.as_expr())
    maximum_values = [abs(lambda_f(float(absolute_maximum))) for absolute_maximum in absolute_maximum_pretenders]
    return max(maximum_values)


def find_d_diff_of_function(function, d: int):
    current_diff = function
    for i in range(0, d):
        current_diff = current_diff.diff(x_symbol)
    return current_diff


def find_theoretical_discrepancy(function, const, degree_of_accuracy, a: np.float64, b: np.float64, h):
    # d - algebraic_degree_of_accuracy
    M = find_absolute_maximum_on_segment(find_d_diff_of_function(function, degree_of_accuracy + 1), x_symbol,
                                         a, b)
    return const * M * (b - a) * pow(h, degree_of_accuracy + 1)


def find_integral_values_on_function(function_lambda, weight_function_lambda, a: np.float64, b: np.float64, m):
    h = float64(find_h(a, b, m))
    value_left, w = left_rectangle_method(function_lambda, weight_function_lambda, a, h, m)
    value_right = right_rectangle_method(function_lambda, weight_function_lambda, a, h, m, w)
    value_middle, q = middle_rectangle_method(function_lambda, weight_function_lambda, a, h, m)
    value_trapezoid, z = trapezoid_method(function_lambda, weight_function_lambda, a, h, m, w)
    value_simpsons = simpsons_method(h, z, w, q)
    return value_left, value_right, value_middle, value_trapezoid, value_simpsons


def test_polynomial(polynomial: Polynomial, degree_of_accuracy: int) -> bool:
    epsilon = float64(pow(10, -7))
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)

    # a = float64(-10)
    # b = float64(10)

    m = pow(10, 5)
    expected = polynomial.integral(b) - polynomial.integral(a)
    values = find_integral_values_on_function(polynomial.polynomial_lambda, weight_function_lambda, a, b, m)
    if degree_of_accuracy == 0:
        start_index = 0
    elif degree_of_accuracy == 1:
        start_index = 2
    elif degree_of_accuracy == 3:
        start_index = 4
    else:
        raise ValueError("WHAT?!")
    for i in range(start_index, len(values)):
        current_actual = values[i]
        discrepancy = find_absolute_discrepancy_value(current_actual, expected)
        if discrepancy > epsilon:
            print(f"Test failed on {i}. Poly: {polynomial.string} Expected = {expected} Actual = {current_actual} Discrepancy = {discrepancy} ")
            return False
    print_green(f"Test passed")
    return True


if __name__ == "__main__":
    user_input = ""

    a = float64(-10)
    b = float64(10)
    function_expression, function_lambda = get_function("x**5")
    m = pow(10, 5)

    while user_input.strip() != "exit":
        # a = get_precise_float(float(input("Enter A: ")))
        # b = get_precise_float(float(input("Enter B: ")))
        # while b <= a:
        #     b = int(input("b must be greater than a. Try again: "))
        #
        # print("Now choose your function:")
        # print("1 -> e^x")
        # print("2 -> 5*x + sin(5*x) + 1")
        # print("3 -> ")
        # print("Enter the number of function to choose:")
        # function_expression, function_lambda = get_function(input("Enter function: "))
        # weight_function_expression, weight_function_lambda = get_function("1")
        #
        # m = int(input("Enter m: "))
        # while m <= 0:
        #     m = int(input("m must be greater than 0. Try again: "))

        J = float64(sympy.integrate(function_expression, (x_symbol, a, b)))
        print(f"Exact value of easily integrated function from a to b: {J}")

        methods = [
            Method(left_rectangle_method, "Left rectangle method"),
            Method(right_rectangle_method, "Right rectangle method"),
            Method(middle_rectangle_method, "Middle rectangle method"),
            Method(trapezoid_method, "Trapezoid method"),
            Method(simpsons_method, "Simpson method"),
        ]

        print("Approximated values of easily integrated function from a to b:")
        value_left, value_right, value_middle, value_trapezoid, value_simpsons = find_integral_values_on_function(
            function_lambda, weight_function_lambda, a, b, m)

        function = sympy.sympify(function_expression)
        h = float64(find_h(a, b, m))
        theoretical_discrepancy_left = find_theoretical_discrepancy(function, float64(1 / 2), 0, a, b, h)
        theoretical_discrepancy_right = find_theoretical_discrepancy(function, float64(1 / 2), 0, a, b, h)
        theoretical_discrepancy_middle = find_theoretical_discrepancy(function, float64(1 / 12), 1, a, b, h)
        theoretical_discrepancy_trapezoid = find_theoretical_discrepancy(function, float64(1 / 24), 1, a, b, h)
        theoretical_discrepancy_simpsons = find_theoretical_discrepancy(function, float64(1 / 2880), 1, a, b, h)

        method_values = [value_left, value_right, value_middle, value_trapezoid, value_simpsons]
        method_theoretical_discrepancies = [theoretical_discrepancy_left, theoretical_discrepancy_right,
                                            theoretical_discrepancy_middle, theoretical_discrepancy_trapezoid,
                                            theoretical_discrepancy_simpsons]

        for method, value, theoretical_discrepancy in zip(methods, method_values, method_theoretical_discrepancies):
            print_red(f"-------{method.name}-------")
            print_method_info(J, value, theoretical_discrepancy)
        print()

        methods_with_0_degree_of_accuracy = methods
        methods_with_1_degree_of_accuracy = methods[2:]
        methods_with_3_degree_of_accuracy = methods[4:]

        print("Tests on polynomials:")

        test_polynomial(polinomial_of_0_degree, 0)
        test_polynomial(polinomial_of_1_degree, 1)
        test_polynomial(polinomial_of_2_degree, 3)
        test_polynomial(polinomial_of_3_degree, 3)
        print()

        user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")
