import copy
import itertools


def fibonacci_numbers_generator():
    for _ in range(2):
        yield "1"
    previous_number = [1]
    current_number = [1]
    while True:
        new_higher_number = []
        add = 0
        for upper_digit, lower_digit in itertools.zip_longest(current_number, previous_number, fillvalue=0):
            add = upper_digit + lower_digit + add
            add, reminder = divmod(add, 10)
            new_higher_number.append(reminder)
        if add != 0:
            new_higher_number.append(add)
        previous_number = copy.copy(current_number)
        current_number = copy.copy(new_higher_number)
        yield "".join(reversed([str(digit) for digit in current_number]))


if __name__ == "__main__":
    number_of_digits = 1_000
    for index, fibonacci_number in enumerate(fibonacci_numbers_generator(), 1):
        if len(fibonacci_number) >= number_of_digits:
            print(index)
            break
