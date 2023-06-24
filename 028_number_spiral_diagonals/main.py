import math


def get_sum_of_diagonals_for_grid(grid_size: int) -> int:
    if grid_size < 1 or grid_size % 2 == 0:
        raise ValueError("Value of 'grid_size' must be greater or equal to 1 and be an odd number!")
    value = 1
    add_number = 1
    for iteration in range(1, math.ceil(grid_size/2)):
        for _ in range(4):
            add_number += iteration*2
            value += add_number
    return value


if __name__ == "__main__":
    print(get_sum_of_diagonals_for_grid(1001))

