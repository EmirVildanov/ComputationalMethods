from tasks.utils.calculation import get_function


def print_task_info():
    print(
        "Theme: Approximate calculation of integrals using quadrature formulas of highest accuracy degree\n"
        "Variant 2. [a, b] = [0, 1], f(x) = sin(x), p(x) = x^(1/4)")
    print()


def print_theory_info():
    print("1. The algebraic degree of accuracy of quadrature formula is a ")
    print("When p(x) is a sign-constant function the algebraic degree of accuracy of"
          "interpolation quadrature formula is a ")
    print("2. The biggest AST of QF with N nodes is")
    print("3. Theorem of QF of Gauss's type: ")
    print("4. The algorithm of building BADA AST (of the biggest algebraic degree of accuracy) with weight function is:")
    print("    1)")
    print("    2)")
    print("    3)")
    print("5. Theorem of BADA AST discrepancy: ")
    print("6. Orthogonal polynomial is a ")
    print("Features of orthogonal polynomial:")
    print("    1)")
    print("    2)")
    print("    3)")
    print("    4)")
    print("    5)")


if __name__ == "__main__":
    print_task_info()

    user_input = ""

    a = float(0)
    b = float(2)
    function_expression, function_lambda = get_function("sin(x)")
    weight_expression, weight_lambda = get_function("x**(1/4)")
    m = pow(10, 5)
    l = 5

    while user_input.strip() != "exit":
        a = float(input("Enter A: "))
        b = float(input("Enter B: "))
        while b <= a:
            b = int(input("b must be greater than a. Try again: "))
        function_expression, function_lambda = get_function(input("Enter function: "))
        weight_function_expression, weight_function_lambda = get_function("1")
        m = int(input("Enter m: "))
        while m <= 0:
            m = int(input("m must be greater than 0. Try again: "))
        l = int(input("Enter l: "))
        while l <= 0:
            l = int(input("l must be greater than 0. Try again: "))

        start_process(a, b, m, l, function_expression, function_lambda)
        user_input = input("If you want to start program, enter 'start'. Otherwise enter 'exit': ")
