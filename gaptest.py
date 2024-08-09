import numpy as np
from scipy.stats import chi2
from tabulate import tabulate

def load_random_numbers(filename, quantity):
    numbers = []
    with open(filename, 'r') as file:
        while len(numbers) < quantity:
            line = file.readline().strip()
            if line:
                try:
                    number = float(line)
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
            if not line:
                break
    if len(numbers) < quantity:
        print(f"Warning: Only {len(numbers)} numbers were read from the file.")
    return numbers

def gap_test(numbers, alpha, low, high):
    gaps = []
    gap = 0
    in_range = False
    for number in numbers:
        if low <= number <= high:
            if in_range:
                gaps.append(gap)
                gap = 0
            in_range = True
        else:
            if in_range:
                gap += 1
    k = len(gaps)
    mean_gap = np.mean(gaps)
    chi_square_stat = (k - mean_gap) ** 2 / mean_gap
    p_value = 1 - chi2.cdf(chi_square_stat, df=k-1)
    if p_value > alpha:
        return "Accepted", k, mean_gap, chi_square_stat, p_value
    else:
        return "Rejected", k, mean_gap, chi_square_stat, p_value

if __name__ == "__main__":
    filename = input("Enter the filename containing random numbers: ")
    quantity = int(input("Enter the number of random numbers to read: "))
    numbers = load_random_numbers(filename, quantity)

    if len(numbers) < quantity:
        print("Not enough data to perform the test.")
    else:
        low = float(input("Enter the lower bound: "))
        high = float(input("Enter the upper bound: "))
        alpha = float(input("Enter the significance level (alpha): "))

        result, k, mean_gap, chi_square_stat, p_value = gap_test(numbers, alpha, low, high)

        table = [["Parameter", "Value"], ["Number of Gaps", k], ["Mean Gap", mean_gap], ["Chi-square Statistic", chi_square_stat], ["P-value", p_value], ["Result", result]]
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
