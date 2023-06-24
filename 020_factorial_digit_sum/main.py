def get_sum_of_factorial_digits(number: int) -> int:
    product = 1
    for current_num in range(2, number + 1):
        product *= current_num
        if str(product)[-1] == "0":
            product = int(str(product)[:-1])
    product = str(product)
    return sum(int(digit) for digit in product)


if __name__ == "__main__":
    print(get_sum_of_factorial_digits(100))
