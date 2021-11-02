from aenum import MultiValueEnum

from tasks.task_1.root_reducer import *


class RootReducerEnum(MultiValueEnum):
    HalfDivisionReducer = HalfDivisionReducer(equation_function), 1
    NewtonReducer = NewtonReducer(equation_function), 2
    ModifiedNewtonReducer = ModifiedNewtonReducer(equation_function), 3
    SecantReducer = SecantReducer(equation_function), 4
