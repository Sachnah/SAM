class MixedLCG:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.current = seed

    def next(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

def main_mixed_lcg():
    # Input parameters from the user
    seed = int(input("Enter the seed (X0): "))
    a = int(input("Enter the multiplier (a): "))
    c = int(input("Enter the increment (c): "))
    m = int(input("Enter the modulus (m): "))

    # Create an instance of the MixedLCG
    mixed_lcg = MixedLCG(seed, a, c, m)

    # Generate 1000 pseudo-random numbers
    print("Mixed LCG:")
    for _ in range(1000):
        print(mixed_lcg.next())

if __name__ == "__main__":
    main_mixed_lcg()
