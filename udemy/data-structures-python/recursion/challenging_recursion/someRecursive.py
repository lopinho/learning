def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 1:
        return cb(arr[0])
    first, *rest = arr
    if cb(first):
        return True
    return someRecursive(rest, cb)