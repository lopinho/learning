
def gcd(first, second):
    first, second = abs(first), abs(second)
    if second > first:
        first, second = second, first
    if first % second == 0:
        return second 
    return gcd(second, first % second)


if __name__ == "__main__":
    print(gcd(8, 12))
    print(gcd(48, 18))