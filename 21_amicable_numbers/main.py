import math
from typing import List


def get_sum_of_proper_divisors(number: int) -> List[int]:
    divisors = [1]
    tmp = math.ceil(math.sqrt(number))
    limit_number = tmp if tmp**2 != number else tmp + 1
    for divisor in range(2, limit_number):
        if number % divisor == 0:
            divisors.append(divisor)
            if (another_divisor := int(number/divisor)) not in divisors:
                divisors.append(another_divisor)
    return sorted(divisors)


def is_number_amicable(number: int) -> bool:
    first_sum = sum(get_sum_of_proper_divisors(number=number))
    second_sum = sum(get_sum_of_proper_divisors(number=first_sum))
    return number == second_sum and first_sum != second_sum


if __name__ == "__main__":
    upper_bound = 10_000
    print(sum(number for number in range(1, upper_bound) if is_number_amicable(number)))
