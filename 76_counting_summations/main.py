import functools
import math


def pentagonal_number(num: int) -> int:
    return num*(3*num - 1)//2


@functools.cache
def number_of_partitions(number: int) -> int:
    """Based on an equation p(n) = Sum (-1)**(k - 1)*p(n - gk), where k != 0 and gk is a pentagonal number.
    https://en.wikipedia.org/wiki/Pentagonal_number_theorem"""
    if number == 0:
        return 1
    num_of_partitions = 0
    k_min = int((1 - math.sqrt(1 + 24*number))/6)
    k_max = int((1 + math.sqrt(1 + 24*number))/6)
    for k in range(k_min, k_max + 1):
        if k == 0:
            continue
        coefficient = int((-1)**(k - 1))
        num_of_partitions += coefficient*number_of_partitions(number - pentagonal_number(k))
    return num_of_partitions


if __name__ == "__main__":
    print(number_of_partitions(100) - 1)
