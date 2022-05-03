def to_bin(n):
    assert int(n) == n and n >= 0, "Allowed only positive integer numbers"
    if n // 2 == 0:
        return n % 2
    return to_bin(n//2) * 10 + n%2


if __name__ == "__main__":
    print(to_bin(1))
    print(to_bin(2))
    print(to_bin(3))
    print(to_bin(4))
    print(to_bin(5))
    print(to_bin(6))
    print(to_bin(7))
    print(to_bin(8))
    print(to_bin(9))
    print(to_bin(10))
    print(to_bin(-1))
    print(to_bin(1.1))