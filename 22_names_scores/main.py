import string

from common import read_file


def sum_word_indexes(word: str) -> int:
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)


if __name__ == "__main__":
    score = 0
    sorted_names = sorted(read_file("p022_names.txt"))
    for word_index, word in enumerate(sorted_names, 1):
        score += word_index*sum_word_indexes(word=word)
    print(score)
