
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return  sorted(str1) == sorted(str2)

if __name__ == "__main__":
    print(is_permutation("1234", "4321"))
    print(is_permutation("124", "4321"))
    print(is_permutation("1254", "4321"))