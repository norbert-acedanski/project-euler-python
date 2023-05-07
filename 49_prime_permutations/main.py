import itertools
from typing import List

from common import prime_number_generator, is_number_prime


def get_permutations_of_number(number: int) -> List[int]:
    """Returns a sorted list of permutation of a given number, that are greater than a given number"""
    permutations = sorted(set(int("".join(num)) for num in itertools.permutations(str(number), r=len(str(number)))))
    return list(filter(lambda num: num > number, permutations))


if __name__ == "__main__":
    first_number = 1487
    for prime in prime_number_generator():
        if prime < 1_000 or prime == first_number:
            continue
        if prime >= 10_000:
            break
        prime_permutations = get_permutations_of_number(prime)
        for combination in itertools.combinations(prime_permutations, r=2):
            second, third = combination
            if second - prime == third - second and is_number_prime(second) and is_number_prime(third):
                print(f"{prime}{second}{third}")
                break
