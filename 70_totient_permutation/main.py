from sympy.ntheory.factor_ import totient


if __name__ == "__main__":
    limit = 10_000_000
    minimum_division_product, n = 100_000_000_000, 2
    for number in range(2, limit):
        if sorted(str(number)) == sorted(str(totient_value := totient(number))) \
                and (division_product := number/totient_value) < minimum_division_product:
            minimum_division_product, n = division_product, number
    print(n)  # Currently, it took almost 13 minutes to compute
