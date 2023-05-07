from math import factorial


def get_upper_limit_for_iteration() -> int:
    """To get this value, we have to solve the inequality:
       max_power*9! <= 10^max_power - 1"""
    max_power = 1
    while True:
        if (limit := max_power*factorial(9)) <= 10**max_power - 1:
            return limit
        else:
            max_power += 1


def is_number_curious(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    return number == sum(factorial(digit) for digit in digits)


if __name__ == "__main__":
    print(sum(number for number in range(3, get_upper_limit_for_iteration() + 1) if is_number_curious(number=number)))
