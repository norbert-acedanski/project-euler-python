from typing import List, Dict


def get_smallest_common_multiple(elements: List[int]) -> int:
    smallest_common_multiple_factors = {}
    for element in elements:
        for factor, power in get_prime_factors(element).items():
            smallest_common_multiple_factors[factor] = power if factor not in smallest_common_multiple_factors \
                else max(smallest_common_multiple_factors[factor], power)
    result = 1
    for factor, power in smallest_common_multiple_factors.items():
        result *= factor**power
    return result


def get_prime_factors(number: int) -> Dict[int, int]:
    prime_factors = {}
    current_factor = 2
    while number > 1:
        if number % current_factor == 0:
            number /= current_factor
            if current_factor not in prime_factors:
                prime_factors[current_factor] = 1
            else:
                prime_factors[current_factor] += 1
        else:
            current_factor += 1
    return prime_factors


if __name__ == "__main__":
    numbers = [num for num in range(2, 21)]
    print(get_smallest_common_multiple(numbers))
