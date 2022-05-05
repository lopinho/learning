def firstSecond(givenList):
    first = 0
    second = 0
    for el in givenList:
        if first < el:
            if first != second:
                second = first
            first = el
    return first, second
                