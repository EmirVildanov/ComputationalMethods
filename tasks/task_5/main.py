from math import cos, pi
from typing import Tuple, Callable, List, Optional

import sympy
from tabulate import tabulate

from tasks.task_1.main import find_equation_root_segments
from tasks.task_1.root_reducer import SecantReducer
from tasks.task_1.task_1_constants import find_h
from tasks.task_4.utils import x_symbol
from tasks.task_5.task_5_constants import *
from tasks.utils.calculation import find_absolute_discrepancy_value, get_function
from tasks.utils.handsome_printer import print_red, print_green


def print_task_info():
    print(
        "Theme: Gauss's quadrature formulas, its nodes and coefficients.\n"
        "Calculation of integrals using Gauss's quadrature formulas")
    print()


def find_legendre_polynomial_value_at_point(n: int, x: float) -> float:
    if n < 0:
        raise RuntimeError(f"Degree of Legendre polynomial must not be negative. Was {n}")
    if n == 0:
        result = 1
    elif n == 1:
        result = x
    else:
        result = ((2 * n - 1) * find_legendre_polynomial_value_at_point(n - 1, x) * x -
                  (n - 1) * find_legendre_polynomial_value_at_point(n - 2, x)) / n
    return result


def find_legendre_polynomial_roots(degree: int, a: float, b: float) -> List[float]:
    function = lambda x: find_legendre_polynomial_value_at_point(degree, x)
    reducer = SecantReducer(function)
    equation_roots = []
    for root_segment in find_equation_root_segments(function, a, b, find_h(pow(10, 5), a, b), False):
        equation_roots.append(reducer.evaluate(root_segment, False))
    return equation_roots


def find_gaussian_coefficient_for_node(n: int, node: float) -> float:
    return (2 * (1 - node ** 2)) / (n ** 2 * find_legendre_polynomial_value_at_point(n - 1, node) ** 2)


def find_gauss_node_to_coefficient_pairs(n: int) -> List[Tuple[float, float]]:
    roots = find_legendre_polynomial_roots(n, -10, 10)
    pairs = []
    for root in roots:
        coefficient = find_gaussian_coefficient_for_node(n, root)
        pairs.append((root, coefficient))
    return pairs


def find_gauss_integral(*, n: int, a: float = -1, b: float = 1,
                        qf_node_to_coefficient_pairs: Optional[List[Tuple[float, float]]] = None,
                        function: Callable) -> float:
    if qf_node_to_coefficient_pairs is not None:
        pairs = qf_node_to_coefficient_pairs
    else:
        pairs = find_gauss_node_to_coefficient_pairs(n)
    integral = 0

    q = (b - a) / 2

    if a != -1 or b != 1:
        print(f"Mapped pairs for N = {n}:")
        pair_table_rows = []
        pair_table_rows.append(["Node", "Coefficient"])
        for pair in pairs:
            pair_table_rows.append([a + q * (pair[0] + 1), pair[1] * q])
        print(tabulate(pair_table_rows))
        print()

    for pair in pairs:
        integral += pair[1] * function(a + q * (pair[0] + 1)) * q
    return integral


def find_meller_integral(*, n: int, a: float = -1, b: float = 1, function: Callable):
    if abs(a) > 1 or abs(b) > 1:
        raise RuntimeError(f"abs(a) and abs(b) must be less then 1. Was: a = {a}, b = {b}")
    integral = 0

    q = (b - a) / 2

    pairs = []
    for k in range(1, n + 1):
        node = cos(((2 * k) - 1) * pi / (2 * n))
        integral += (pi / n) * function(a + q * (node + 1)) * q
        pairs.append((node, pi / n))
    return integral, pairs


def test_polynomial(polynomial: Polynomial, degree_of_accuracy: int,
                    pairs_list: List[List[Tuple[float, float]]]) -> bool:
    epsilon = pow(10, -12)
    # a = random.uniform(-100, 100)
    # b = random.uniform(a, 100)
    a = -1
    b = 1
    expected = polynomial.integral(b) - polynomial.integral(a)
    actual = find_gauss_integral(n=degree_of_accuracy, qf_node_to_coefficient_pairs=pairs_list[degree_of_accuracy - 1],
                                 function=polynomial.polynomial_lambda)
    discrepancy = find_absolute_discrepancy_value(actual, expected)
    if discrepancy > epsilon:
        print_red(
            f"Test failed on {polynomial.string}.\n"
            f"n: {degree_of_accuracy}\n"
            f"a: {a}, b: {b},\n"
            f"Expected: {expected},\n"
            f"Actual: {actual},\n"
            f"Discrepancy = {discrepancy} ")
        return False
    print_green(f"Test passed on {polynomial.string}")
    return True


def print_node_to_coefficients_pairs_info(pairs: List[Tuple[float, float]]):
    for pair in pairs:
        print(f"{pair[0]} -> {pair[1]}")


def calculate_gauss_example(pairs: List[List[Tuple[float, float]]]):
    print("Calculation of Gauss example function:")
    print(string_for_gauss_qf)
    print()

    # a = float(input("Enter a: "))
    # b = float(input("Enter b: "))
    a = -1
    b = 1

    table_rows = []
    header_row = ["N", "Value", "Discrepancy"]
    table_rows.append(header_row)

    function_expression, function_lambda = get_function(expression_for_gauss_qf)
    actual_integral = float(sympy.integrate(function_expression, (x_symbol, a, b)))
    print(f"Actual value: {actual_integral}")
    for n in n_values_for_chosen_gauss_integral:
        gauss_integral = find_gauss_integral(n=n, a=a, b=b, function=lambda_for_gauss_qf, qf_node_to_coefficient_pairs=pairs[n - 1])
        discrepancy = find_absolute_discrepancy_value(actual_integral, gauss_integral)
        table_rows.append([n, gauss_integral, discrepancy])
    print("Table of results:")
    print(tabulate(table_rows))
    print()


def calculate_meller_example():
    print("Calculation of Meller example function:")
    print(string_for_meller_qf)
    print()


    # n_1 = int(input("Enter N1: "))
    # n_2 = int(input("Enter N2: "))
    # n_3 = int(input("Enter N3: "))
    n_1 = 3
    n_2 = 4
    n_3 = 5

    table_rows = []
    header_row = ["N", "Value", "Discrepancy"]
    table_rows.append(header_row)

    function_expression, function_lambda = get_function(expression_for_meller_qf)
    actual_integral = float(sympy.integrate(function_expression, (x_symbol, -1, 1)))
    print(f"Actual value: {actual_integral}")

    for n in (n_1, n_2, n_3):
        meller_integral, pairs = find_meller_integral(n=n, a=-1, b=1, function=lambda_for_meller_qf)
        discrepancy = find_absolute_discrepancy_value(actual_integral, meller_integral)
        table_rows.append([n, meller_integral, discrepancy])
        print(f"Pairs for N = {n}")
        pair_table_rows = []
        pair_table_rows.append(["Node", "Coefficient"])
        for pair in pairs:
            pair_table_rows.append([pair[0], f"{pair[1]} (pi / {n})"])
        print(tabulate(pair_table_rows))
        print()
    print("Table of results:")
    print(tabulate(table_rows))


if __name__ == "__main__":
    print_task_info()

    print("Gauss's QF:")
    print("Node -> coefficient")
    gauss_node_to_coefficient_pairs_list = []

    for n in range(1, 9):
        current_pairs = find_gauss_node_to_coefficient_pairs(n)
        gauss_node_to_coefficient_pairs_list.append(current_pairs)
        print(f"Current pairs for {n}")
        print_node_to_coefficients_pairs_info(current_pairs)
        print()

    n_values_to_test_polynomials = [1, 2, 3, 4, 5]
    polynomials = [polynomial_of_1_degree, polynomial_of_3_degree, polynomial_of_5_degree, polynomial_of_7_degree,
                   polynomial_of_9_degree]
    print("Testing quadrature formulas on polynomials:")
    for n_value, polynomial in zip(n_values_to_test_polynomials, polynomials):
        test_polynomial(polynomial, n_value, gauss_node_to_coefficient_pairs_list)
    print()

    calculate_gauss_example(gauss_node_to_coefficient_pairs_list)
    calculate_meller_example()
