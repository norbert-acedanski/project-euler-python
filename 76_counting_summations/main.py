def number_of_partitions(number: int) -> int:
    if number < 2:
        raise ValueError("Number should be higher than 1!")
    num_of_partitions = 1
    current_partition = [number - 1, 1]
    print(current_partition)
    while set(current_partition) != {1}:
        first_element = current_partition[0]
        if set(current_partition) == {first_element, 1}:
            if first_element - 1 >= (second_element := current_partition[1]) + 1:
                if first_element - 1 >= (sum_without_first := sum(current_partition) - first_element) + 1:
                    current_partition = [first_element - 1, sum_without_first + 1]
                else:
                    # Error for number == 7 -> [4, 1, 1, 1] -> [3, 2, 1, 1]
                    current_partition = [first_element - 1, second_element + 1, *current_partition[2:]]
            else:
                # Error for number == 7 -> [3, 3, 1] -> [3, 2, 1, 1]
                current_partition[current_partition.index(1) - 1] -= 1
                current_partition.append(1)
        else:
            first_one_index = current_partition.index(1) if 1 in current_partition else -1
            if first_one_index == -1:
                current_partition = [*current_partition[:-1], current_partition[-1] - 1, 1]
            else:
                if current_partition[first_one_index - 1] != 2:
                    current_partition = [*current_partition[:-first_one_index], current_partition[-first_one_index] - 1, 2, *current_partition[-first_one_index + 1:]]
                else:
                    current_partition = [*current_partition[:-first_one_index], *[1]*(first_one_index + 1)]
        num_of_partitions += 1
        print(current_partition)
    return num_of_partitions


if __name__ == "__main__":
    print(f"Number of partitions: {number_of_partitions(7)}", end="\n\n")
