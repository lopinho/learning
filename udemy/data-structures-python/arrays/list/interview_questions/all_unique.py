

def all_unique(arr):
    processed = []
    for el in arr:
        if el in processed:
            return False
        processed.append(el)
    return True


if __name__ == "__main__":
    print(all_unique([1,2,3,4,5,6]))
    print(all_unique([1,2,3,4,5,6, 1]))