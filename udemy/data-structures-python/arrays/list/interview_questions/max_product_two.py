
def find_max_product(arr):
    max_product = 0
    for i, val1 in enumerate(arr[:-1]):
        for j in range(i+1, len(arr)):
            product = val1 * arr[j]
            if product > max_product:
                max_product = product
    return max_product

if __name__ == "__main__":
    print(find_max_product([1,2,3,4,5,6,8]))
    print(find_max_product([8,6,8, 9, 10]))

    