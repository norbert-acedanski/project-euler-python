from math import factorial
from functools import cache


@cache
def factorial_sum_from_a_number(number: int) -> int:
    return sum(factorial(int(digit)) for digit in str(number))


if __name__ == "__main__":
    limit = 1_000_000
    number_of_non_repeating_terms = 60
    numbers_with_desired_number_of_non_repeating_terms = []
    for num in range(3, limit):
        non_repeating_values = [num]
        factorial_product = num
        while (new_product := factorial_sum_from_a_number(factorial_product)) not in non_repeating_values:
            non_repeating_values.append(new_product)
            factorial_product = new_product
            if len(non_repeating_values) == number_of_non_repeating_terms:
                numbers_with_desired_number_of_non_repeating_terms.append(num)
                break
    print(len(numbers_with_desired_number_of_non_repeating_terms))
