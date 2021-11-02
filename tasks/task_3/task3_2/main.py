import numpy as np
from tabulate import tabulate

from tasks.task_2.main import print_table_values
from tasks.task_3.task3_2.task_3_2_constants import *


def print_task_info():
    print("Theme: Finding the derivatives of a table-defined function by numerical differentiation formulas")
    print("Variant 2")


def find_first_derivatives(given_x, given_y, h):
    first_derivatives = []
    n = len(given_x) - 1
    for i in range(n - 1):
        first_derivatives.append((-3 * given_y[i] + 4 * given_y[i + 1] - given_y[i + 2]) / (2 * h))
    first_derivatives.append((3 * given_y[n - 1] - 4 * given_y[n - 2] + given_y[n - 3]) / (2 * h))
    first_derivatives.append((3 * given_y[n] - 4 * given_y[n - 1] + given_y[n - 2]) / (2 * h))

    return first_derivatives


def find_second_derivatives(given_x, given_y, h):
    second_derivatives = ["UNKNOWN"]
    for i in range(1, len(given_x) - 1):
        second_derivatives.append((given_y[i + 1] - 2 * given_y[i] + given_y[i - 1]) / (h ** 2))
    second_derivatives.append("UNKNOWN")

    return second_derivatives


def print_results_table(table_of_values, h):
    given_x = [pair[0] for pair in table_of_values]
    given_y = [pair[1] for pair in table_of_values]
    first_derivatives = find_first_derivatives(given_x, given_y, h)
    second_derivatives = find_second_derivatives(given_x, given_y, h)
    table = []
    first_row = ["x_i", "f(x_i)", "f'(x_i)_чд", "|f'(x_i)_т - f'(x_i)_чд|", "f''(x_i)", "|f''(x_i)_т - f''(x_i)_чд|"]
    table.append(first_row)
    for i in range(len(table_of_values)):
        x_i = given_x[i]
        y_i = given_y[i]
        first_derivative = first_derivatives[i]
        second_derivative = second_derivatives[i]
        given_first_derivative = given_function_first_derivative(x_i)
        given_second_derivative = given_function_second_derivative(x_i)
        first_diff = abs(given_first_derivative - first_derivative)
        if second_derivative != "UNKNOWN":
            second_diff = abs(given_second_derivative - second_derivative)
        else:
            second_diff = "UNKNOWN"
        current_row = [x_i, y_i, first_derivative, first_diff, second_derivative, second_diff]
        table.append(current_row)
    print(tabulate(table))


if __name__ == "__main__":
    print_task_info()
    user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")

    number_of_values = 31
    a = 0
    h = 10 ** (-10)  # plot step

    while user_input.strip() != "exit":
        a = float(input("Enter the start point: "))
        h = float(input("Enter the base of h: "))
        h_power = int(input("Enter the power of h: "))
        h = pow(h, h_power)
        number_of_values = int(input("Enter the number of values: "))
        m = number_of_values - 1

        formula_for_x_i = lambda i: a + i * h

        b = formula_for_x_i(m)
        given_x_range = np.arange(a, b + h, h)

        print(f"Number of values: {number_of_values}")
        print()
        table_of_values = [(x, given_function(x)) for x in [formula_for_x_i(i) for i in range(0, number_of_values)]]
        print("Table of values:")
        print_table_values(table_of_values)
        print("Results table:")
        print_results_table(table_of_values, h)

        user_input = input("To start program again enter 'start'. Otherwise enter 'exit': ")
