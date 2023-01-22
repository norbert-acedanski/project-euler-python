def get_number_of_solutions_for_perimeter(perimeter_value: int) -> int:
    number_of_solutions = 0
    if perimeter_value % 2 != 0:
        return 0
    duplicates = []
    for a in range(1, perimeter_value//2 + 1):
        for b in range(1, perimeter_value//2):
            c = perimeter_value - a - b
            if (a, b, c) not in duplicates and is_triple_right_triangle(a, b, c):
                number_of_solutions += 1
                duplicates.append((a, b, c))
    return number_of_solutions


def is_triple_right_triangle(a: int, b: int, c: int) -> bool:
    return True if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else False


if __name__ == "__main__":
    target = 1000
    max_solutions_perimeter = 4
    max_solutions = 1
    for perimeter in range(4, target + 1):
        if (new_max := get_number_of_solutions_for_perimeter(perimeter_value=perimeter)) > max_solutions:
            max_solutions = new_max
            max_solutions_perimeter = perimeter
    print(max_solutions_perimeter)
