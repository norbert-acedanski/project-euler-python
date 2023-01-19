import itertools


if __name__ == "__main__":
    number_of_digits = 10
    target_index = 1_000_000
    for index, permutation in enumerate(itertools.permutations(range(number_of_digits), number_of_digits), 1):
        if index == target_index:
            print("".join(str(digit) for digit in permutation))
            break
