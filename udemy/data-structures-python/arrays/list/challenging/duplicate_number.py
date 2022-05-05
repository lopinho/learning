def removeDuplicates(myList):
    # return list(set(myList))
    uniques = []
    for el in myList:
        if el not in uniques:
            uniques.append(el)
    return uniques