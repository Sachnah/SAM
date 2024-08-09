# KS Test

import numpy as np
from tabulate import tabulate
from scipy.stats import kstest


# np.random.seed(42)
# random_numbers = np.random.uniform(0, 1, 15)
with open("random.txt", "r") as file:
    random_numbers = list(int(line.strip()) for line in file.readlines())

ks_results = []
alpha = 0.05

for i in range(1, len(random_numbers) + 1):
    sample = random_numbers[:i]
    ks_statistic, p_value = kstest(sample, 'uniform')
    status = 'Pass' if p_value > alpha else 'Fail'
    ks_results.append((ks_statistic, p_value, sample[-1], status))

table = [
    ['Random Number', 'KS Statistic', 'P-value', 'Status']
]

for ks_stat, p_val, num, status in ks_results:
    table.append([num, ks_stat, p_val, status])

print(tabulate(table, headers='firstrow', tablefmt='grid'))
