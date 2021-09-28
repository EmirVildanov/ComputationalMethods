from math import log

import numpy as np

a = 0
b = 1
plot_step = 0.1
given_x_range = np.arange(a, b + plot_step, plot_step)

given_function = lambda x: log(1 + x)
formula_for_x_i = lambda i, m: a + i * (b - a) / m