
def firbonacci(n):
    assert n >= 0 and int(n) == n, "Allowed only positive integer numbers" #Unintentional case
    if n < 2: # Exit condition
        return n
    return firbonacci(n-1) + firbonacci(n-2) # Recursive condition


if __name__ == "__main__":
    print(firbonacci(0))
    print(firbonacci(1))
    print(firbonacci(2))
    print(firbonacci(3))
    print(firbonacci(4))
    print(firbonacci(5))
    print(firbonacci(6))
    print(firbonacci(7))
    print(firbonacci(7.5))
    print(firbonacci(-1))
