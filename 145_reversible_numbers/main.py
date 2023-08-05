def is_number_reversible(number: int) -> bool:
    return not {"0", "2", "4", "6", "8"}.intersection(str(number + int(str(number)[::-1])))


if __name__ == "__main__":
    number_of_reversible_numbers = 0
    limit = 10**9
    for number in range(1, limit):
        if not str(number).endswith("0") and is_number_reversible(number=number):
            number_of_reversible_numbers += 1
    print(number_of_reversible_numbers)  # It takes ~30 minutes to print the answer for now...
