from typing import List


def get_abundant_numbers_lower_than(upper_bound: int) -> List[int]:
    return [number for number in range(1, upper_bound + 1) if is_number_abundant(number)]


def is_number_abundant(number: int) -> bool:
    sum_of_divisors = sum(divisor for divisor in range(1, number//2 + 1) if number % divisor == 0)
    return sum_of_divisors > number


def get_sum_of_numbers_that_cannot_be_written_as_sum_of_two_abundant_numbers(upper_bound: int) -> int:
    abundant_numbers = get_abundant_numbers_lower_than(upper_bound=upper_bound)
    sum_numbers = {num_1 + num_2 for index, num_1 in enumerate(abundant_numbers) for num_2 in abundant_numbers[index:]}
    return sum(set(range(1, upper_bound + 1)).difference(sum_numbers))


if __name__ == "__main__":
    upper_limit = 28_123
    print(get_sum_of_numbers_that_cannot_be_written_as_sum_of_two_abundant_numbers(upper_bound=upper_limit))
