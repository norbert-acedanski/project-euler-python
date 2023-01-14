from typing import List


def get_prime_factors(number: int) -> List[int]:
    prime_factors = set()
    current_factor = 2
    while number > 1:
        if number % current_factor == 0:
            number /= current_factor
            prime_factors.add(current_factor)
        else:
            current_factor += 1
    return list(prime_factors)


if __name__ == "__main__":
    print(max(get_prime_factors(600851475143)))
