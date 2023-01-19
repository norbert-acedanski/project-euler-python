from typing import List


def get_last_digits_for_max_power(power: int, number_of_digits: int) -> str:
    if power < 1:
        raise ValueError("Power value must be positive!")
    if power < 1:
        raise ValueError("Number of digits be at least 1!")
    digits = [0]*number_of_digits
    digits[0] = 1
    for current_power in range(2, power + 1):
        add = 0
        calculated_number = calculate_large_exponent_n_last_digits(base=current_power, exponent=current_power,
                                                                   n=number_of_digits)
        for index in range(number_of_digits):
            current_add = digits[index] + calculated_number[index] + add
            digits[index] = current_add % 10
            add = current_add // 10
    return "".join(str(digit) for digit in reversed(digits))


def calculate_large_exponent_n_last_digits(base: int, exponent: int, n: int) -> List[int]:
    digits = list(int(digit) for digit in reversed(str(base)))
    digits += [0]*(n - len(digits))
    for _ in range(exponent - 1):
        add = 0
        for index in range(len(digits)):
            current_multiple = digits[index]*base
            digits[index] = (current_multiple + add) % 10
            add = (current_multiple + add)//10
    return digits


if __name__ == "__main__":
    max_power = 1000
    print(get_last_digits_for_max_power(power=max_power, number_of_digits=10))
