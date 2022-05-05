def missingNumber(myList, totalCount):
    total = totalCount * (totalCount +1) /2
    return total - sum(myList)