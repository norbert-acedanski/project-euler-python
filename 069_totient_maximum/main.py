from sympy.ntheory.factor_ import totient


if __name__ == "__main__":
    limit = 1_000_000
    maximum_division_product, n = 1, 2
    for number in range(2, limit + 1):
        if (division_product := number/totient(number)) > maximum_division_product:
            maximum_division_product, n = division_product, number
    print(n)  # Currently, it took almost a minute to compute
