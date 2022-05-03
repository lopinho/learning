def productOfArray(arr):
    if len(arr) == 1:
        return arr[0]
    first,second, *rest = arr
    rest.append(first*second)
    return productOfArray(rest)