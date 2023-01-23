def calculate_large_exponent(base: int, exponent: int) -> str:
    digits = list(int(digit) for digit in reversed(str(base)))
    add = 0
    for _ in range(exponent - 1):
        for index in range(len(digits)):
            current_multiple = digits[index]*base
            # Replacement of add = (current_multiple + add)//10 and digits[index] = (current_multiple + add) % 10
            add, digits[index] = divmod(current_multiple + add, 10)
        if add != 0:
            digits.append(add)
            add = 0
    return "".join(reversed([str(digit) for digit in digits]))


if __name__ == "__main__":
    base_number = 2
    power = 1000
    print(sum(int(digit) for digit in calculate_large_exponent(base=base_number, exponent=power)))
