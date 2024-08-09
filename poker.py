import itertools
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

def poker_test(numbers, alpha):
    n = len(numbers)
    counts = {comb: 0 for comb in itertools.combinations_with_replacement('0123456789', 5)}
    for number in numbers:
        digits = str(number).replace('.', '')[:5]
        counts[tuple(sorted(digits))] += 1
    expected = n / len(counts)
    chi_square_stat = sum((count - expected) ** 2 / expected for count in counts.values())
    p_value = 1 - chi2.cdf(chi_square_stat, df=len(counts) - 1)
    if p_value > alpha:
        return "Accepted", chi_square_stat, p_value
    else:
        return "Rejected", chi_square_stat, p_value

if __name__ == "__main__":
    filename = input("Enter the filename containing random numbers: ")
    quantity = int(input("Enter the number of random numbers to read: "))
    numbers = load_random_numbers(filename, quantity)

    if len(numbers) < quantity:
        print("Not enough data to perform the test.")
    else:
        alpha = float(input("Enter the significance level (alpha): "))

        result, chi_square_stat, p_value = poker_test(numbers, alpha)

        table = [["Parameter", "Value"], ["Chi-square Statistic", chi_square_stat], ["P-value", p_value], ["Result", result]]
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
