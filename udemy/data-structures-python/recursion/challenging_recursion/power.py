def power(base, exponent):
    assert int(exponent) == exponent and exponent >=0
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

