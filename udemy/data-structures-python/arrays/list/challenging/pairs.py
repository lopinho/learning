def pairSum(myList, target):
    results = []
    for i, el1 in enumerate(myList[:-1]):
        for el2 in myList[i+1:]:
            if el1 + el2 == target:
                results.append("{}+{}".format(el1, el2))
    return results