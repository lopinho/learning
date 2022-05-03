def factorial(num):
    assert int(num) == num and num > 0
    if num == 1:
        return 1
    return num * factorial(num-1)