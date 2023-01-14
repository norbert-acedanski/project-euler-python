from typing import Tuple


def find_pythagorean_triplets_based_on_their_sum(expected_sum: int) -> Tuple[int, int, int]:
    for largest in range(1, expected_sum - 1):
        for middle in range(1, largest):
            for smallest in range(1, middle):
                if smallest**2 + middle**2 == largest**2 and smallest + middle + largest == expected_sum:
                    return smallest, middle, largest


if __name__ == "__main__":
    a, b, c = find_pythagorean_triplets_based_on_their_sum(1000)
    print(a*b*c)
