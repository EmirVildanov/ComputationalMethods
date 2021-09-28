from aenum import MultiValueEnum

from tasks.task_1.root_reducer import *


class RootReducerEnum(MultiValueEnum):
    HalfDivisionReducer = HalfDivisionReducer(), 1
    NewtonReducer = NewtonReducer(), 2
    ModifiedNewtonReducer = ModifiedNewtonReducer(), 3
    SecantReducer = SecantReducer(), 4
