
def sum_digits(n:int) -> int:
    assert n >= 0 and int(n) == n, "Number must be a positive integer"
    if n / 10 < 1:
        return n % 10
    return n % 10 + sum_digits(n//10)

if __name__ == "__main__":
    print(sum_digits(10))
    print(sum_digits(45))
    print(sum_digits(112))
    print(sum_digits(-2))
    print(sum_digits(3.1))
