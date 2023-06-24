def are_multiples_of_a_number_permuted(number: int, max_multiple: int) -> bool:
    for current_multiple in range(2, max_multiple + 1):
        if sorted(str(number)) != sorted(str(number*current_multiple)):
            return False
    return True


if __name__ == "__main__":
    current_number_to_check = 100
    maximum_multiple = 6
    while True:
        if (new_power := len(str(current_number_to_check*6))) > len(str(current_number_to_check)):
            current_number_to_check = 10**(new_power - 1)
        if are_multiples_of_a_number_permuted(number=current_number_to_check, max_multiple=maximum_multiple):
            break
        current_number_to_check += 1
    print(current_number_to_check)
