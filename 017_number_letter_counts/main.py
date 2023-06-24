number_word_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
dozen_numbers_word_dict = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                           15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
ten_digits_word_dict = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
                        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
dicta = {0: number_word_dict, 1: ten_digits_word_dict}


def _get_partial_word_representation(index: int, digit: str) -> str:
    if index == 3:
        return number_word_dict[int(digit)] + " thousand "
    elif (index + 1) % 3 == 0:
        return number_word_dict[int(digit)] + " hundred "
    elif (index + 2) % 3 == 0:
        return ten_digits_word_dict[int(digit)] + " "


def get_word_representation_of_a_number(number: int) -> str:
    if number >= 10**6:
        raise ValueError("For now, the function accepts only number up to 10^4")
    number = str(number)
    word_representation = ""
    for index, digit in zip(range(len(number) - 1, -1, -1), number):
        if index == 1 and digit == "1":
            word_representation += dozen_numbers_word_dict[int(f"{digit}{number[-1]}")]
            break
        if digit != "0":
            if index == 0:
                word_representation += number_word_dict[int(digit)]
            else:
                word_representation += _get_partial_word_representation(index=index, digit=digit)
        if index == 2 and (number[-2] != "0" or number[-1] != "0"):
            word_representation += "and "
    return word_representation.strip()


if __name__ == "__main__":
    letter_count = 0
    from_number = 1
    to_number = 1000
    for num in range(from_number, to_number + 1):
        for word in get_word_representation_of_a_number(num).split():
            letter_count += len(word)
    print(letter_count)
