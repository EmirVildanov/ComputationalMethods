from tasks.task_1.task_1_constants import *
from tasks.utils.handsome_printer import print_red


class RootReducer:
    def __init__(self, method_name, method_function, equation_function):
        self.method_name = method_name
        self.method_function = method_function
        self.equation_function = equation_function

    def evaluate(self, segment, print_info=True):
        reduction_steps_counter, result_x, delta = self.method_function(segment)

        if print_info:
            print_red(f"--------{self.method_name}--------")
            print(f"Start segment: {segment}")
            print(f"Number of reduction steps: {reduction_steps_counter}")
            print(f"Reducted root: {result_x}")
            print(f"Length of last reduction segment: {delta}")
            print(f"Absolute value of discrepancy: {abs(self.equation_function(result_x))}")
            print()
        return result_x


class SecantReducer(RootReducer):
    def __init__(self, equation_function):
        super().__init__("Secant method", self.method_function, equation_function)

    def method_function(self, segment):
        reduction_steps_counter = 0

        previous_point = None
        current_point = segment[0]


        while previous_point is None or (abs(current_point - previous_point) > epsilon):
            reduction_steps_counter += 1

            if previous_point is None:
                previous_previous_point = segment[1]
            else:
                previous_previous_point = previous_point
            previous_previous_function_value = self.equation_function(previous_previous_point)

            previous_point = current_point
            previous_function_value = self.equation_function(previous_point)

            current_point = previous_point - previous_function_value * (previous_point - previous_previous_point) / (
                    previous_function_value - previous_previous_function_value
            )

        delta = current_point - previous_point

        return reduction_steps_counter, current_point, delta


class ModifiedNewtonReducer(RootReducer):
    def __init__(self, equation_function):
        super().__init__("Modified Newton method", self.method_function, equation_function)

    def method_function(self, segment):
        reduction_steps_counter = 0

        start_point = segment[0]
        current_point = start_point
        previous_point = None
        while previous_point is None or abs(current_point - previous_point) >= epsilon:
            previous_point = current_point
            current_point = previous_point - self.equation_function(previous_point) / first_equation_function_derivative(
                start_point)
            reduction_steps_counter += 1

        delta = current_point - previous_point
        return reduction_steps_counter, current_point, delta


class HalfDivisionReducer(RootReducer):
    def __init__(self, equation_function):
        super().__init__("Half division method", self.method_function, equation_function)

    def method_function(self, segment):
        reduction_steps_counter = 0
        a = segment[0]
        b = segment[1]
        while b - a > 2 * epsilon:
            c = (a + b) / 2
            if self.equation_function(a) * self.equation_function(c) <= 0:
                b = c
            else:
                a = c
            reduction_steps_counter += 1
        x = (a + b) / 2
        delta = b - a

        return reduction_steps_counter, x, delta


class NewtonReducer(RootReducer):
    def __init__(self, equation_function):
        super().__init__("Newton method", self.method_function, equation_function)

    def method_function(self, segment):
        reduction_steps_counter = 0
        current_point = segment[0]
        previous_point = None
        while previous_point is None or abs(current_point - previous_point) >= epsilon:
            previous_point = current_point
            current_point = previous_point - self.equation_function(previous_point) / first_equation_function_derivative(
                previous_point)
            reduction_steps_counter += 1

        delta = current_point - previous_point

        return reduction_steps_counter, current_point, delta
