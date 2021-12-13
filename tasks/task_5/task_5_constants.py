from math import sqrt, exp

from tasks.task_4.task_4_constants import Polynomial

polynomial_of_1_degree = Polynomial(
    lambda x: x - 3,
    lambda x: x ** 2 / 2 - 3 * x,
    "x - 3"
)
polynomial_of_3_degree = Polynomial(
    # (x - 1)(x - 2)(x - 3)
    lambda x: x ** 3 - 6 * x ** 2 + 11 * x - 6,
    lambda x: x ** 4 / 4 - 2 * x ** 3 + 11 * x ** 2 / 2 - 6 * x,
    "x^3 - 6x^2 + 11x - 6"
)
polynomial_of_5_degree = Polynomial(
    lambda x: x ** 5 + 9 * x ** 4 - 53 * x ** 3 + 309 * x ** 2 + 592 * x - 2640,
    lambda x: x ** 6 / 6 + 9 * x ** 5 / 5 - 53 * x ** 4 / 4 + 103 * x ** 3 + 296 * x ** 2 - 2640 * x,
    "x^5 + 9x^4 - 53x^3 + 309x^2 + 592x - 2640"
)
polynomial_of_7_degree = Polynomial(
    lambda x: x ** 7 - 12 * x ** 6 + 26 * x ** 5 + 148 * x ** 4 - 711 * x ** 3 + 752 * x ** 2 + 564 * x - 1008,
    lambda x: x ** 8 / 8 - 12 * x ** 7 / 7 + 13 * x ** 6 / 3 + 148 * x ** 5 / 5 - 711 * x ** 4 / 4 + 752 * x ** 3 / 3 + 282 * x ** 2 - 1008 * x,
    "8x^7 + 42x^5 + 12x^2 + 69"
)
polynomial_of_9_degree = Polynomial(
    lambda x: x ** 9 - 9 * x ** 8 + 29 * x ** 7 - 35 * x ** 6 - 6 * x ** 5 + 44 * x ** 4 - 24 * x ** 3,
    lambda x: x ** 10 / 10 - x ** 9 + 29 * x ** 8 / 8 - 5 * x ** 7 - x ** 6 + 44 * x ** 5 / 5 - 6 * x ** 4,
    "20x^9 + 56x^3 + 33x^2"
)

lambda_for_gauss_qf = lambda x: (2.175 * x ** 5 - 3.267 * x ** 2 + 6.321) / sqrt((1 - x ** 2))
expression_for_gauss_qf = "(2.175 * x ** 5 - 3.267 * x ** 2 + 6.321) / sqrt(1 + x**2)"
n_values_for_chosen_gauss_integral = [3, 5]
string_for_gauss_qf = "1 / sqrt((1 + x^2)(4 + 3x^2)) dx from 0 to 1"

lambda_for_meller_qf = lambda x: (2.175 * x ** 5 - 3.267 * x ** 2 + 6.321)
expression_for_meller_qf = "(2.175 * x ** 5 - 3.267 * x ** 2 + 6.321) / sqrt(1 - x**2)"
fixed_lambda_for_meller_qf = lambda x: (2.175 * x ** 5 - 3.267 * x ** 2 + 6.321) / sqrt(1 - x ** 2)
n_values_for_chosen_meller_integral = [1, 2, 3]
string_for_meller_qf = "exp(2x) / sqrt(1 - x^2) dx from -1 to 1"
