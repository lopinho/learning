
def missing(arr, length):
    return sorted(set(range(1, length+1)) - set(arr))

def missing_one(arr, length):
    total = length * (length+1)/2
    return total - sum(arr)



if __name__ == "__main__":
    print(missing([1,2,3,4,5,8], 10))
    print(missing_one([1,2,3,4,5,6,8,9,10], 10))