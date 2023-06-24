from math import factorial


def n_for_r(n: int, r: int) -> int:
    return int(factorial(n)/(factorial(r)*factorial(n - r)))


if __name__ == "__main__":
    n_max_value, answer = 100, 0
    for n in range(1, n_max_value + 1):
        for r in range(1, n + 1):
            if n_for_r(n, r) > 1_000_000:
                answer += 1
    print(answer)
