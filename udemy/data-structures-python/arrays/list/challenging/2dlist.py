
def sumDiagonal(a):
    rows = len(a)
    columns = len(a[0])
    total = 0
    for i in range(rows):
        for j in range(columns):
            if i==j:
                total += a[i][j]
    return total