def digit_square_end_loop_number(number: int) -> int:
    end_loop_numbers = [1, 89]
    digit_square = number
    while True:
        if digit_square in end_loop_numbers:
            return digit_square
        digit_square = sum(int(digit)**2 for digit in str(digit_square))


if __name__ == "__main__":
    limit = 10_000_000
    target_end_number = 89
    no_of_numbers = 0
    for num in range(1, limit):
        if digit_square_end_loop_number(number=num) == target_end_number:
            no_of_numbers += 1
    print(no_of_numbers)
