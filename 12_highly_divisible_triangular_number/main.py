def get_triangular_numbers_generator():
    triangular_number = 1
    boundary = 1
    while True:
        yield triangular_number
        boundary += 1
        triangular_number += boundary


def get_number_of_divisors_of_a_number(number: int) -> int:
    num_of_divisors = 2
    for divisor in range(2, number//2 + 1):
        if number % divisor == 0:
            num_of_divisors += 1
    return num_of_divisors


if __name__ == "__main__":
    number_of_divisors = 500
    for num in get_triangular_numbers_generator():
        if get_number_of_divisors_of_a_number(num) > number_of_divisors:
            print(num)  # To get here it took 2h 51min...
            break
