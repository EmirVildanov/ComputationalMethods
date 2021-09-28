import warnings
from pprint import pprint

from task_2_constants import *

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')


def print_task_info():
    print("Theme: Algebraic interpolation")
    print("Variant 2")
    print(f"a: {a}")
    print(f"b: {b}")


def find_divided_diff(x_array, y_array):
    table_side = len(y_array)
    coefficients = np.zeros([table_side, table_side])
    coefficients[:, 0] = y_array

    for j in range(1, table_side):
        for i in range(table_side - j):
            coefficients[i][j] = \
                (coefficients[i + 1][j - 1] - coefficients[i][j - 1]) / (x_array[i + j] - x_array[i])

    return coefficients


def find_newton_polynomial(x_data, coefficients, x_range):
    polynomial = coefficients[len(coefficients) - 1]
    for k in range(1, len(coefficients)):
        polynomial = coefficients[len(coefficients) - 1 - k] + (x_range - x_data[len(x_data) - 1 - k]) * polynomial
    return polynomial


def find_newton_interpolated_value(x_for_test, given_x, given_y):
    coefficients = find_divided_diff(given_x, given_y)[0, :]
    y_linearized = find_newton_polynomial(given_x, coefficients, given_x_range)
    interpolated_value_of_test_point = find_newton_polynomial(given_x, coefficients, np.float64([x_for_test]))[0]
    return y_linearized, interpolated_value_of_test_point


def find_lagrange_interpolated_value(x_for_test, given_x, given_y):
    interpolated_value = 0

    for i in range(len(given_x)):
        polynomial = 1

        for j in range(len(given_x)):
            if i != j:
                polynomial = polynomial * (x_for_test - given_x[j]) / (given_x[i] - given_x[j])

        interpolated_value += polynomial * given_y[i]

    return interpolated_value


def is_x_for_test_in_points(x, points):
    for point in points:
        if point == x:
            return True
    return False


def start_interpolation_process_with_values(sorted_table_of_values, x_for_test):
    given_x = np.float64([pair[0] for pair in sorted_table_of_values])
    given_y = np.float64([pair[1] for pair in sorted_table_of_values])

    y_linearized, newton_interpolated_value = find_newton_interpolated_value(x_for_test, given_x, given_y)
    lagrange_interpolated_value = find_lagrange_interpolated_value(x_for_test, given_x, given_y)

    value_of_given_function_in_test_x = given_function(x_for_test)
    print(f"Value of given function at {x_for_test} is {value_of_given_function_in_test_x}")
    print(f"Newton interpolated value at {x_for_test} is {newton_interpolated_value}.")
    print(f"Lagrange interpolated value at {x_for_test} is {lagrange_interpolated_value}.")
    print(
        f"Absolute value of Newton method discrepancy: {abs(newton_interpolated_value - value_of_given_function_in_test_x)}")
    print(
        f"Absolute value of Lagrange method discrepancy: {abs(lagrange_interpolated_value - value_of_given_function_in_test_x)}")
    print()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        plt.figure(figsize=(12, 8))
        plt.plot(x_for_test, newton_interpolated_value, 'ro', color='black')
        plt.plot(x_for_test, given_function(x_for_test), 'ro', color='red')
        plt.plot(given_x, given_y, 'bo')
        plt.plot(given_x_range, y_linearized)
        plt.show()


if __name__ == "__main__":
    print_task_info()
    user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")

    m = 15
    x_for_test = 0.35
    n = 7

    while user_input.strip() != "exit":
        number_of_values = int(input("Enter the number of values in the table: "))
        m = number_of_values - 1

        table_of_values = [(x, given_function(x)) for x in [formula_for_x_i(i, m) for i in range(0, m)]]
        print(f"Number of values: {m + 1}")
        print("Table of values:")
        pprint(table_of_values)
        print()

        x_for_test = float(input("Enter point's x you want to interpolate: "))
        while x_for_test <= -1:
            x_for_test = float(input("x must be greater than -1. Try again: "))

        n = int(input(f"Enter the degree of interpolation polynomial (from [{2}-{m}] range): "))
        while 2 > n or n > m:
            n = int(input("You entered incorrect value. Try again: "))
        print()

        sorted_table_of_values = sorted(table_of_values, key=lambda pair: abs(pair[0] - x_for_test))[0:n]
        print("Sorted table of values: ")
        pprint(sorted_table_of_values)
        print()

        start_interpolation_process_with_values(sorted_table_of_values, x_for_test)
        user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")
