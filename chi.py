import numpy as np
from tabulate import tabulate
from scipy.stats import chisquare

# Read the random numbers from the file and convert them to floats
with open("random.txt", "r") as file:
    random_numbers = list(float(line.strip()) for line in file.readlines())

# Set the number of bins and adjust the range based on the data
num_bins = 10
min_value = min(random_numbers)
max_value = max(random_numbers)

observed_frequencies, edges = np.histogram(random_numbers, bins=num_bins, range=(min_value, max_value))
expected_frequencies = np.ones(num_bins) * (len(random_numbers) / num_bins)
chi_statistic, p_value = chisquare(observed_frequencies, expected_frequencies)

print(f"Chi-Square Statistic: {chi_statistic}")
print(f"P-value: {p_value}")

alpha = 0.05
status = 'Pass' if p_value > alpha else 'Fail'
print(f"Test Status: {status}")

table = [
    ['S.N', 'Range', 'Observed Frequency', 'Expected Frequency']
]

for i, (obs, exp) in enumerate(zip(observed_frequencies, expected_frequencies)):
    table.append([i + 1, f'({edges[i]:.1f}, {edges[i + 1]:.1f})', obs, exp])

print(tabulate(table, headers='firstrow', tablefmt='grid'))
