def factorial(n: int):
    assert n >= 0 and int(n) == n, "The number must be a positive integer" # Unintentional case
    if 0 <= n <= 1: # Stopping criterion
        return 1
    return n * factorial(n-1) # 1- Recursive case


if __name__ == "__main__":
    print(factorial(1))
    print(factorial(2))
    print(factorial(3))
    print(factorial(4))
    print(factorial(5))
    print(factorial(6))
    print(factorial(7))
    print(factorial(8))
    print(factorial(-8))
    print(factorial(8.5))