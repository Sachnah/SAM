import numpy as np
from scipy.special import erfinv
from tabulate import tabulate

def load_random_numbers(filename, quantity):
    numbers = []
    with open(filename, 'r') as file:
        while len(numbers) < quantity:
            line = file.readline().strip()
            if line:  # Only process non-empty lines
                try:
                    number = float(line)
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
            if not line:  # Stop reading if end of file is reached
                break
    if len(numbers) < quantity:
        print(f"Warning: Only {len(numbers)} numbers were read from the file.")
    return numbers

def autocorrelation_test(numbers, lag, alpha):
    n = len(numbers)
    mean = np.mean(numbers)
    numerator = sum((numbers[i] - mean) * (numbers[i + lag] - mean) for i in range(n - lag))
    denominator = sum((numbers[i] - mean) ** 2 for i in range(n))
    rho = numerator / denominator
    Z0 = rho * np.sqrt(n / (1 - rho ** 2))
    Z_alpha = np.sqrt(2) * erfinv(1 - alpha)
    if abs(Z0) < Z_alpha:
        return "Accepted", rho, Z0, Z_alpha
    else:
        return "Rejected", rho, Z0, Z_alpha

if __name__ == "__main__":
    filename = input("Enter the filename containing random numbers: ")
    quantity = int(input("Enter the number of random numbers to read: "))
    numbers = load_random_numbers(filename, quantity)

    if len(numbers) < quantity:
        print("Not enough data to perform the test.")
    else:
        lag = int(input("Enter the lag (k): "))
        alpha = float(input("Enter the significance level (alpha): "))

        result, rho, Z0, Z_alpha = autocorrelation_test(numbers, lag, alpha)
        
        table = [["Parameter", "Value"], ["Mean", np.mean(numbers)], ["Rho", rho], ["Z0", Z0], ["Z_alpha", Z_alpha], ["Result", result]]
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
