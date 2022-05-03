def capitalizeFirst(arr):
    first, *rest = arr
    first = [first.capitalize()]
    if len(rest) == 0:
        return first
    return first + capitalizeFirst(rest)
    