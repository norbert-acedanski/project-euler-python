from common import read_file, sum_word_indexes


if __name__ == "__main__":
    score = 0
    sorted_names = sorted(read_file("p022_names.txt"))
    for word_index, word in enumerate(sorted_names, 1):
        score += word_index*sum_word_indexes(word=word)
    print(score)
