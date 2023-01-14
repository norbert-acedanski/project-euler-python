def fibonacci_numbers(up_to: int):
    current_number = 1
    yield current_number
    next_number = 2
    while next_number < up_to:
        yield next_number
        current_number, next_number = next_number, current_number + next_number


if __name__ == "__main__":
    print(sum(fibonacci_number for fibonacci_number in fibonacci_numbers(4_000_000) if not fibonacci_number % 2))
