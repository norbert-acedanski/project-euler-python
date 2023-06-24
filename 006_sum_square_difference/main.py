def get_sum_of_squares(up_to: int) -> int:
    return sum((number**2 for number in range(1, up_to + 1)))


def get_square_of_sum_of_numbers(up_to: int) -> int:
    return int((1 + up_to)*up_to/2)**2


if __name__ == "__main__":
    max_number = 100
    print(get_square_of_sum_of_numbers(max_number) - get_sum_of_squares(max_number))
