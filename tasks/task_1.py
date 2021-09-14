from math import sin, log, cos


def equation_function(x):
    return pow(2, -x) - sin(x)


def first_equation_function_derivative(x):
    return -pow(2, -x) * log(2) - cos(x)


def second_equation_function_derivative(x):
    return pow(2, -x) * pow(log(2), 2) + sin(x)


def find_h(n: int):
    if n < 2:
        raise RuntimeError(f"Broken N argument: {n}. It should be greater than 1")
    return (B - A) / n


task_theme = "Numerical methods for solving nonlinear equations"
A = -5
B = 10
N = pow(10, 3)
h = find_h(N)
epsilon = pow(10, -6)
equation_function_string_view = "2^(-x) - sin(x)"


def print_start_info():
    print(task_theme)
    print(f"Parameter A: {A}")
    print(f"Parameter B: {B}")
    print(f"Parameter epsilon: {epsilon}")
    print(f"Parameter function: {equation_function_string_view}")


def find_equation_root_segments():
    root_segments = []
    counter = 0
    x1 = A
    x2 = x1 + h
    y1 = equation_function(x1)
    while x2 <= B:
        y2 = equation_function(x2)
        if y1 * y2 <= 0:
            counter += 1
            current_root_segment = (x1, x2)
            root_segments.append(current_root_segment)
            print(f"Current root segment: {current_root_segment}")
        x1 = x2
        x2 = x1 + h
        y1 = y2
    print(f"Root segments number: {counter}")
    print()
    return root_segments


def half_division_method(segment):
    reduction_steps_counter = 0
    print("Half division method")
    print(f"Start segment: {segment}")

    a = segment[0]
    b = segment[1]
    while b - a > 2 * epsilon:
        c = (a + b) / 2
        if equation_function(a) * equation_function(c) <= 0:
            b = c
        else:
            a = c
        reduction_steps_counter += 1
    x = (a + b) / 2
    delta = (b - a) / 2

    print(f"Number of reduction steps: {reduction_steps_counter}")
    print(f"Reducted root: {x}")
    print(f"Length of last reduction segment: {delta}")
    print(f"Absolute value of discrepancy: {abs(equation_function(x))}")
    print()


def modified_newton_method(segment):
    reduction_steps_counter = 0
    print("Newton method")
    print(f"Start segment: {segment}")

    current_point = segment[0]
    previous_point = None
    while previous_point is None or abs(current_point - previous_point) >= epsilon:
        previous_point = current_point
        current_point = previous_point - equation_function(previous_point) / first_equation_function_derivative(
            previous_point)
        reduction_steps_counter += 1

    print(f"Number of reduction steps: {reduction_steps_counter}")
    print(f"Reducted root: {current_point}")
    print(f"Absolute value of discrepancy: {abs(equation_function(current_point))}")
    print()

    reduction_steps_counter = 0
    print("Newton method")
    print(f"Start segment: {segment}")

    start_point = segment[0]
    current_point = start_point
    previous_point = None
    while previous_point is None or abs(current_point - previous_point) >= epsilon:
        previous_point = current_point
        current_point = previous_point - equation_function(previous_point) / first_equation_function_derivative(
            start_point)
        reduction_steps_counter += 1

    print(f"Number of reduction steps: {reduction_steps_counter}")
    print(f"Reducted root: {current_point}")
    print(f"Absolute value of discrepancy: {abs(equation_function(current_point))}")
    print()


def secant_method(segment):
    reduction_steps_counter = 0
    print("Secant method")
    print(f"Start segment: {segment}")

    previous_point = None
    previous_function_value = None
    current_point = segment[0]

    while previous_point is None or (abs(current_point - previous_point) > epsilon):
        reduction_steps_counter += 1

        if previous_point is None:
            previous_previous_point = segment[1]
            prev_prev_function_value = equation_function(previous_previous_point)
        else:
            previous_previous_point = previous_point
            prev_prev_function_value = previous_function_value

        previous_point = current_point
        previous_function_value = equation_function(previous_point)

        current_point = previous_point - previous_function_value * (previous_point - previous_previous_point) / (
                previous_function_value - prev_prev_function_value
        )

    print(f"Number of reduction steps: {reduction_steps_counter}")
    print(f"Reducted root: {current_point}")
    print(f"Absolute value of discrepancy: {abs(equation_function(current_point))}")
    print()


if __name__ == "__main__":
    print_start_info()
    for root_segment in find_equation_root_segments():
        modified_newton_method(root_segment)
