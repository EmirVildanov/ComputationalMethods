from math import log, e

import numpy as np

given_function = lambda x: log(1 + x)
reversed_given_function = lambda x: e ** x - 1
# given_function = lambda x: e ** x
# reversed_given_function = lambda x: log(x)
formula_for_x_i = lambda i, m: a + i * (b - a) / m

a = 0
b = 1
plot_step = 0.1
given_x_range = np.arange(a, b + plot_step, plot_step)
given_y_range = np.arange(reversed_given_function(a + plot_step), reversed_given_function(b) + plot_step * 2, plot_step)

