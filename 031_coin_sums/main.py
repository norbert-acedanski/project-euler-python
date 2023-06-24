from typing import List


def multiply_two_polynomials(A: List[int], B: List[int]) -> List[int]:
    product = [0]*(len(A) + len(B) + 1)
    for a_coefficient in range(len(A)):
        for b_coefficient in range(len(B)):
            product[a_coefficient + b_coefficient] += A[a_coefficient]*B[b_coefficient]
    return product


if __name__ == "__main__":
    available_coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target_coin_change = 200
    polynomials = [[0 if power % coin else 1 for power in range(0, target_coin_change + 1)] for coin in available_coins]
    polynomial_product = polynomials[0]
    for polynomial in polynomials[1:]:
        polynomial_product = multiply_two_polynomials(A=polynomial_product, B=polynomial)
    print(polynomial_product[target_coin_change])
