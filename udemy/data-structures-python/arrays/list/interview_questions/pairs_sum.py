from collections import defaultdict

def pair_sum(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            first = arr[i]
            second = arr[j]
            if first + second == target and first != second:
                result.append([i, j])
    return result



if __name__ == "__main__":
    print(pair_sum([2,7,11,15], 9))
    print(pair_sum([3,2,4,3], 6))
    print(pair_sum([3,3], 6))
    print(pair_sum([1,2,3, 2, 3, 4, 5, 6], 6))