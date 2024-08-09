class MultiplicativeLCG:
    def __init__(self, seed, a, m):
        self.seed = seed
        self.a = a
        self.m = m
        self.current = seed

    def next(self):
        self.current = (self.a * self.current) % self.m
        return self.current

def main_multiplicative_lcg():
    # Input parameters from the user
    seed = int(input("Enter the seed (X0): "))
    a = int(input("Enter the multiplier (a): "))
    m = int(input("Enter the modulus (m): "))

    # Create an instance of the MultiplicativeLCG
    multiplicative_lcg = MultiplicativeLCG(seed, a, m)

    # Generate 1000 pseudo-random numbers
    print("Multiplicative LCG:")
    for _ in range(1000):
        print(multiplicative_lcg.next())

if __name__ == "__main__":
    main_multiplicative_lcg()
