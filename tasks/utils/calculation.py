from sympy import parse_expr, lambdify

from tasks.task_4.task4_2.task4_2_constants import DEFAULT_FUNCTION_VALUE


def find_absolute_discrepancy_value(expected, actual):
    return abs(expected - actual)


def get_function(input: str):
    try:
        f_default = parse_expr(DEFAULT_FUNCTION_VALUE)
        f_default_lambda = lambdify("x", f_default)
    except Exception as e:
        print(e)
        raise Exception("Given default function is invalid")

    try:
        f = parse_expr(input)
        f_lambda = lambdify("x", f)
    except Exception as e:
        print(e)
        f = f_default
        f_lambda = f_default_lambda

    return f, f_lambda
