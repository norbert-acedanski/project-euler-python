def get_collatz_number_of_terms(number: int) -> int:
    terms = 1
    while number != 1:
        number = number/2 if number % 2 == 0 else 3*number + 1
        terms += 1
    return terms


if __name__ == "__main__":
    maximum_number = 1_000_000
    highest_number_of_terms = 0
    longest_chain_number = 1
    for num in range(1, maximum_number):
        if (new_highest := get_collatz_number_of_terms(num)) > highest_number_of_terms:
            highest_number_of_terms = new_highest
            longest_chain_number = num
    print(longest_chain_number)
