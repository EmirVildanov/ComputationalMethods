from math import e


class Polynomial():
    def __init__(self, polynomial, integral, string):
        self.polynomial_lambda = polynomial
        self.integral = integral
        self.string = string


easily_integrated_function = lambda x: e ** x
integral_for_easily_integrated_function = lambda a, b: e ** b - e ** a
weight_p_for_easily_integrated_function = lambda x: 1

polinomial_of_0_degree = Polynomial(lambda x: 42,
                                    lambda x: 42 * x,
                                    "42")
polinomial_of_1_degree = Polynomial(lambda x: 11 + 38 * x,
                                    lambda x: 11 * x + 19 * x ** 2,
                                    "11 + 38x")
polinomial_of_2_degree = Polynomial(lambda x: 53 + 20 * x + 9 * x ** 2,
                                    lambda x: 53 * x + 10 * x ** 2 + 3 * x ** 3,
                                    "53 + 20x + 9x^2")
polinomial_of_3_degree = Polynomial(lambda x: 97 + 4 * x + 24 * x ** 2 + 4 * x ** 3,
                                    lambda x: 97 * x + 2 * x ** 2 + 8 * x ** 3 + x ** 4,
                                    "97 + 3x + 24x^2 + 4x^3")
