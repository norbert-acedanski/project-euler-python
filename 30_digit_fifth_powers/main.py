def get_upper_limit_for_iteration(power: int) -> int:
    number_of_digits = 1
    while (limit := number_of_digits*9**power) > 10**number_of_digits:
        number_of_digits += 1
    return limit


def is_number_sum_of_its_digits_raised_to_a_power(number: int, power: int) -> bool:
    number_str = str(number)
    return number == sum(int(digit)**power for digit in number_str)


if __name__ == "__main__":
    power_value = 5
    numbers_list = []
    for num in range(2, get_upper_limit_for_iteration(power=power_value) + 1):
        if is_number_sum_of_its_digits_raised_to_a_power(number=num, power=power_value):
            numbers_list.append(num)
    print(sum(numbers_list))
