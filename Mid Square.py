import random

seed = 4567
num_digits = 4


def mid_square(quantity):
    global seed
    seed_length = len(str(seed))
    if seed_length != num_digits:
        raise ValueError("Seed must have the specified number of digits")
    random_numbers = []
    for _ in range(quantity):
        squared = seed ** 2
        squared_str = str(squared).zfill(num_digits * 2)

        mid_start = (len(squared_str) - num_digits) // 2
        mid_end = mid_start + num_digits
        seed = int(squared_str[mid_start:mid_end])
        random_numbers.append(seed)
    return random_numbers


if __name__ == "__main__":
    random_numbers = mid_square(1000)
    print(random_numbers)
    with open("random.txt", "w") as file:
        for number in random_numbers:
            file.write(f"{number}\n")