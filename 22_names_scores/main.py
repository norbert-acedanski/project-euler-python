from typing import List
import string


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        data = file.readline()
    return data[1:-1].split('","')


def sum_word_indexes(word: str) -> int:
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)


if __name__ == "__main__":
    score = 0
    sorted_names = sorted(read_file("p022_names.txt"))
    for word_index, word in enumerate(sorted_names, 1):
        score += word_index*sum_word_indexes(word=word)
    print(score)
