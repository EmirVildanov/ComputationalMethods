import warnings

import numpy as np
from matplotlib import pyplot as plt

from tasks.task_1.main import find_equation_root_segments
from tasks.task_1.root_reducer import SecantReducer
from tasks.task_1.task_1_constants import find_h
from tasks.task_2.main import print_table_values
from tasks.task_3.task3_1.task_3_1_constants import a, b, given_function, formula_for_x_i, given_x_range, given_y_range, \
    reversed_given_function


def print_task_info():
    print("Theme: Reverse interpolation")
    print("Variant 2")
    print(f"a: {a}")
    print(f"b: {b}")


def find_newton_interpolated_value_for_point(x, given_x, given_y):
    def find_divided_diff(x_array, y_array):
        table_side = len(y_array)
        coefficients = np.zeros([table_side, table_side])
        coefficients[:, 0] = y_array

        for j in range(1, table_side):
            for i in range(table_side - j):
                coefficients[i][j] = \
                    (coefficients[i + 1][j - 1] - coefficients[i][j - 1]) / (x_array[i + j] - x_array[i])

        return coefficients

    coefficients = find_divided_diff(given_x, given_y)[0, :]

    polynomial_value_at_point = coefficients[len(coefficients) - 1]
    for k in range(1, len(coefficients)):
        polynomial_value_at_point = coefficients[len(coefficients) - 1 - k] + (
                x - given_x[len(given_x) - 1 - k]) * polynomial_value_at_point
    return polynomial_value_at_point


def find_lagrange_interpolated_value_for_point(x, given_x, given_y):
    interpolated_value = 0

    for i in range(len(given_x)):
        polynomial = 1

        for j in range(len(given_x)):
            if i != j:
                polynomial = polynomial * (x - given_x[j]) / (given_x[i] - given_x[j])

        interpolated_value += polynomial * given_y[i]

    return interpolated_value


def is_x_for_test_in_points(x, points):
    for point in points:
        if point == x:
            return True
    return False


def draw_plot_for_values(x_for_test, given_x, given_y, x_range, y_range, interpolated_value):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        plt.figure(figsize=(12, 8))
        plt.plot(x_for_test, interpolated_value, 'ro', color='black')
        plt.plot(x_for_test, given_function(x_for_test), 'ro', color='red')
        plt.plot(given_x, given_y, 'bo')
        plt.plot(x_range, y_range)
        plt.show()


def reversed_function_variant(sorted_table_of_values, F_to_test):
    given_y = np.float64([pair[0] for pair in sorted_table_of_values])
    given_x = np.float64([pair[1] for pair in sorted_table_of_values])

    x_linearized = np.array([find_newton_interpolated_value_for_point(y, given_y, given_x) for y in given_y_range])
    newton_interpolated_value = find_newton_interpolated_value_for_point(F_to_test, given_y, given_x)

    value_of_given_function_in_test_x = reversed_given_function(F_to_test)
    print(f"Newton interpolated value at {F_to_test} is {newton_interpolated_value}")
    print(
        f"Absolute value of first method discrepancy: {abs(newton_interpolated_value - value_of_given_function_in_test_x)}")
    print()

    # draw_plot_for_values(F_to_test, given_y, given_x, x_linearized, given_y_range, newton_interpolated_value)


def secant_method_root_reducer_variant(table_of_values, F_to_test):
    given_x = np.float64([pair[0] for pair in table_of_values])
    given_y = np.float64([pair[1] for pair in table_of_values])
    y_linearized = np.array([find_newton_interpolated_value_for_point(x, given_x, given_y) for x in given_x_range])

    function = lambda x: find_newton_interpolated_value_for_point(x, given_x, given_y) - F_to_test
    reducer = SecantReducer(function)
    equation_answers = []
    for root_segment in find_equation_root_segments(function, a, b, find_h(pow(10, 3), a, b), False):
        equation_answers.append(reducer.evaluate(root_segment, False))
    if len(equation_answers) > 1:
        raise RuntimeError(
            f"More than one root was found."
            f"\nRoots: {equation_answers}."
            f"\nValues at answers: {[given_function(answer) for answer in equation_answers]}")
    answer = equation_answers[0]
    draw_plot_for_values(answer, given_x, given_y, given_x_range, y_linearized, given_function(answer))
    print(f"Secant reduced value at {F_to_test} is {answer}")
    print(
        f"Absolute value second method discrepancy: {abs(answer - reversed_given_function(F_to_test))}")


if __name__ == "__main__":
    print_task_info()
    user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")

    # number_of_values = 30
    # F_to_find = 0.3
    # n = 29
    # number_of_values = 3
    # F_to_find = -2.75
    # n = 2

    while user_input.strip() != "exit":
        number_of_values = int(input("Enter the number of values in the table: "))
        m = number_of_values - 1

        print(f"Number of values: {number_of_values}")
        table_of_values = [(x, given_function(x)) for x in [formula_for_x_i(i, m) for i in range(0, number_of_values)]]
        print("Table of values:")
        print_table_values(table_of_values)

        F_to_test = float(input("Enter point's F you want to test: "))

        n = int(input(f"Enter the degree of interpolation polynomial (from [{2}-{m}] range): "))
        while 2 > n or n > m:
            n = int(input("You entered incorrect value. Try again: "))
        print()

        reversed_table_of_values = [(pair[1], pair[0]) for pair in table_of_values]
        print("Reversed table of values:")
        print_table_values(reversed_table_of_values)
        sorted_table_of_reversed_values = sorted(reversed_table_of_values, key=lambda pair: abs(pair[0] - F_to_test))
        print("Sorted table of reversed values:")
        print_table_values(sorted_table_of_reversed_values[0:n + 1])

        nearest_argument_to_F = sorted(table_of_values, key=lambda pair: abs(pair[1] - F_to_test))
        reversed_function_variant(sorted_table_of_reversed_values[0:n + 1], F_to_test)

        print("Sorted table of values:")
        print_table_values(nearest_argument_to_F[0:n + 1])
        secant_method_root_reducer_variant(nearest_argument_to_F[0:n + 1], F_to_test)

        user_input = input("To start program again enter 'start'. Otherwise enter 'exit': ")
