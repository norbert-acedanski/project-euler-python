from common import get_reduced_fractions

if __name__ == "__main__":
    reduced_fractions = get_reduced_fractions(12_000)
    print(reduced_fractions.index((1, 2)) - reduced_fractions.index((1, 3)) - 1)  # It took almost 2 minutes
