from tasks.task_1.root_reducer_enum import RootReducerEnum
from tasks.task_1.task_1_constants import *


def print_start_info():
    print(task_title)
    print(f"Parameter A: {A}")
    print(f"Parameter B: {B}")
    print(f"Parameter epsilon: {epsilon}")
    print(f"Parameter function: {equation_function_string_view}")
    print()


def find_equation_root_segments(function, A, B, h, print_info=True):
    root_segments = []
    counter = 0
    x1 = A
    x2 = x1 + h
    y1 = function(x1)
    while x2 <= B:
        y2 = function(x2)
        if y1 * y2 <= 0:
            counter += 1
            current_root_segment = (x1, x2)
            root_segments.append(current_root_segment)
            if print_info:
                print(f"Current root segment: {current_root_segment}")
        x1 = x2
        x2 = x1 + h
        y1 = y2
    if print_info:
        print(f"Root segments number: {counter}")
        print()
    return root_segments


def start_interactive_evaluation():
    while True:
        print("What reducing method do you want to use?")
        for reducer in list(RootReducerEnum):
            print(f"{reducer.name} -> {reducer.values[1]}")
        print("Exit program -> Enter any another symbol")
        try:
            chosen_reducer = RootReducerEnum(int(input("Enter number: ")))
            print()
            for root_segment in find_equation_root_segments(equation_function, A, B, h):
                chosen_reducer.values[0].evaluate(root_segment)
        except ValueError:
            print("Exiting program")
            break


def start_simple_evaluation():
    for root_segment in find_equation_root_segments(equation_function, A, B, h):
        print(f"WORKING ON SEGMENT {root_segment}:")
        for reducer in list(RootReducerEnum):
            reducer.values[0].evaluate(root_segment)


if __name__ == "__main__":
    print_start_info()
    start_simple_evaluation()
