import sympy

# 4)Уточнить  значения  J(h) и J(h/l) по принципу Рунге для каждой СКФ.
# 5)Посчитать и вывести на печать абсолютные фактические погрешности для уточнённых значений.

# Test:
# Протестировать программу для случая, когда искомое значение интеграла довольно велико
# (подобрать такие f(x) и [A, B]). «Поиграть» числом разбиений m(от 10 000 до 1 000 000).
# •Убедиться, что СКФ Симпсона при умеренном числе разбиений(1000, 10000)
# дает результат, более точный чем при миллионе.
# •Подумать, с чем может быть связана потеря точности «у Симпсона»
from tabulate import tabulate

from tasks.task_4.task4_2.main import *
from tasks.task_4.utils import x_symbol, weight_function_lambda, find_h, Method
from tasks.utils.calculation import get_function


def print_method_info(J, actual, actual_l, refined, theoretical_discrepancy):
    print(f"Precise: {J}")
    print(f"Actual: {actual}")
    print(f"Actual_l: {actual_l}")
    print(f"Refined: {refined}")
    actual_absolute_discrepancy = find_absolute_discrepancy_value(J, actual)
    actual_absolute_discrepancy_l = find_absolute_discrepancy_value(J, actual_l)
    refined_absolute_discrepancy = find_absolute_discrepancy_value(J, refined)
    print(f"Absolute value of discrepancy: {actual_absolute_discrepancy}")
    print(f"Absolute value of discrepancy_l: {actual_absolute_discrepancy_l}")
    print(f"Absolute value of discrepancy_refine: {refined_absolute_discrepancy}")

    print(f"Theoretical discrepancy: {theoretical_discrepancy}")
    print(
        f"Discrepancies' diff: {find_absolute_discrepancy_value(actual_absolute_discrepancy, theoretical_discrepancy)}")
    print(
        f"Discrepancies' diff_l: {find_absolute_discrepancy_value(actual_absolute_discrepancy_l, theoretical_discrepancy)}")


def start_process(a, b, m, l, function_expression, function_lambda):
    J = float(sympy.integrate(function_expression, (x_symbol, a, b)))
    print(f"Exact value of easily integrated function from a to b: {J}")

    methods = [
        Method(left_rectangle_method, "Left rectangle method"),
        Method(right_rectangle_method, "Right rectangle method"),
        Method(middle_rectangle_method, "Middle rectangle method"),
        Method(trapezoid_method, "Trapezoid method"),
        Method(simpsons_method, "Simpson method"),
    ]

    value_left, value_right, value_middle, value_trapezoid, value_simpsons = find_integral_values_on_function(
        function_lambda, weight_function_lambda, a, b, m)

    value_left_l, value_right_l, value_middle_l, value_trapezoid_l, value_simpsons_l = find_integral_values_on_function(
        function_lambda, weight_function_lambda, a, b, m * l)

    function = sympy.sympify(function_expression)
    h = float(find_h(a, b, m))
    theoretical_discrepancy_left = find_theoretical_discrepancy(function, float(1 / 2), 0, a, b, h)
    theoretical_discrepancy_right = find_theoretical_discrepancy(function, float(1 / 2), 0, a, b, h)
    theoretical_discrepancy_middle = find_theoretical_discrepancy(function, float(1 / 12), 1, a, b, h)
    theoretical_discrepancy_trapezoid = find_theoretical_discrepancy(function, float(1 / 24), 1, a, b, h)
    theoretical_discrepancy_simpsons = find_theoretical_discrepancy(function, float(1 / 2880), 3, a, b, h)

    method_values = [value_left, value_right, value_middle, value_trapezoid, value_simpsons]
    method_values_l = [value_left_l, value_right_l, value_middle_l, value_trapezoid_l, value_simpsons_l]
    method_theoretical_discrepancies = [theoretical_discrepancy_left, theoretical_discrepancy_right,
                                        theoretical_discrepancy_middle, theoretical_discrepancy_trapezoid,
                                        theoretical_discrepancy_simpsons]

    refined_values = []
    for triple in zip(method_values, method_values_l, [0, 0, 1, 1, 3]):
        r = triple[2] + 1
        refined_values.append((l ** r * triple[1] - triple[0]) / (l ** r - 1))

    table_rows = []
    header_row = ["Method name", "J(h)", "J(h/l)", "R", "|J(h) - J|", "|J(h / l) - J|", "|R - J|", "Theoretical"]
    table_rows.append(header_row)

    print("Table of actual values:")
    for method, value, value_l, refined_value, theoretical_discrepancy in zip(methods, method_values, method_values_l,
                                                                              refined_values,
                                                                              method_theoretical_discrepancies):
        actual_absolute_discrepancy = find_absolute_discrepancy_value(J, value)
        actual_absolute_discrepancy_l = find_absolute_discrepancy_value(J, value_l)
        refined_absolute_discrepancy = find_absolute_discrepancy_value(J, refined_value)
        table_rows.append(
            [method.name, value, value_l, refined_value, actual_absolute_discrepancy, actual_absolute_discrepancy_l,
             refined_absolute_discrepancy, theoretical_discrepancy])
    print(tabulate(table_rows))
    print()

    print("Tests on polynomials:")
    test_polynomial(polinomial_of_0_degree, 0)
    test_polynomial(polinomial_of_1_degree, 1)
    test_polynomial(polinomial_of_2_degree, 3)
    test_polynomial(polinomial_of_3_degree, 3)
    print()


if __name__ == "__main__":
    print_task_info()

    user_input = ""

    a = float(1)
    b = float(5)
    function_expression, function_lambda = get_function("x**2 + 33 * x + 402")
    m = pow(10, 5)
    l = 5

    while user_input.strip() != "exit":
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))
        while b <= a:
            b = int(input("b must be greater than a. Try again: "))
        function_expression, function_lambda = get_function(input("Enter function: "))
        weight_function_expression, weight_function_lambda = get_function("1")
        m = int(input("Enter m: "))
        while m <= 0:
            m = int(input("m must be greater than 0. Try again: "))
        l = int(input("Enter l: "))
        while l <= 0:
            l = int(input("l must be greater than 0. Try again: "))

        start_process(a, b, m, l, function_expression, function_lambda)
        user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")
