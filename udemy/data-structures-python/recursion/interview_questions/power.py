
def power(base, exp):
    assert exp == int(exp) and exp >= 0, "Allowed only positive and integer expoents"
    if exp == 0:
        return 1 
    return base * power(base, exp-1)

if __name__ == "__main__":
    print(power(4, 0))
    print(power(4, 3))
    print(power(2, 3))