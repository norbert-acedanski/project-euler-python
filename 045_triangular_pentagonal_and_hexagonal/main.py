import math


def triangle_number(n: int) -> int:
    return n*(n + 1)//2


def is_number_pentagonal(n: int) -> bool:
    index = (1 + math.sqrt(1 + 24*n))/6
    return index == int(index)


def is_number_hexagonal(n: int) -> bool:
    index = (1 + math.sqrt(1 + 8*n))/4
    return index == int(index)


if __name__ == "__main__":
    number = 286
    while True:
        triangle_num = triangle_number(number)
        if is_number_pentagonal(triangle_num) and is_number_hexagonal(triangle_num):
            print(triangle_num)
            break
        number += 1
