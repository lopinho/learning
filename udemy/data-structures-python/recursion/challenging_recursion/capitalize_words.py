def capitalizeWords(arr):
    first, *rest = arr
    first = [first.upper()]
    if len(rest) == 0:
        return first
    return first + capitalizeWords(rest)