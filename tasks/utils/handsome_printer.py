from tabulate import tabulate


def print_red(text):
    WARNING = '\033[91m'
    ENDC = '\033[0m'
    print(f"{WARNING}{text}{ENDC}")


def print_table_values(table):
    table_rows = []
    header_row = ["x", "f(x)"]
    table_rows.append(header_row)
    for pair in table:
        table_rows.append([pair[0], pair[1]])
    print(tabulate(table_rows))