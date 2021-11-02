from math import e

given_function = lambda x: e ** (4.5 * x)
given_function_first_derivative = lambda x: 4.5 * e ** (4.5 * x)
given_function_second_derivative = lambda x: 20.25 * e ** (4.5 * x)