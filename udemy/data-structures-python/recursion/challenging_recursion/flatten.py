def flatten(arr):
    if len(arr) == 0:
        return []
    first, *rest = arr
    if isinstance(first, list):
        first = flatten(first)
    else:
        first = [first]
    return first + flatten(rest)