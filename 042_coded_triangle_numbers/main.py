from string import ascii_uppercase
from typing import List

from common import read_file, sum_word_indexes


def get_list_of_triangular_number_below(value: int) -> List[int]:
    triangular_numbers_list = [1]
    index = 1
    while triangular_numbers_list[-1] < value:
        index += 1
        triangular_numbers_list.append(int(0.5*index*(index + 1)))
    return triangular_numbers_list


if __name__ == "__main__":
    sorted_words = sorted(read_file("p042_words.txt"))
    max_word_length = len(max(sorted_words, key=len))
    triangular_numbers = get_list_of_triangular_number_below(value=(max_word_length + 1)*len(ascii_uppercase))
    number_of_triangular_words = 0
    for word in sorted_words:
        if sum_word_indexes(word=word) in triangular_numbers:
            number_of_triangular_words += 1
    print(number_of_triangular_words)
