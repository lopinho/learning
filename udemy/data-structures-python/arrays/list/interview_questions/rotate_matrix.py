

def rotate_right(matriz):
    rols = len(matriz)
    columns = len(matriz[0])
    rotated = [[0]*columns for _ in range(rols)]

    for i in range(rols):
        for j in range(columns):
            rotated[j][columns-i-1] = matriz[i][j]
    return rotated


def rotate_inplace(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

def print_matriz(matriz):
    print("")
    for line in matriz:
        for cell in line:
            print("{:02} ".format(cell), end="")
        print("")

if __name__ == "__main__":
    matriz = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    print_matriz(matriz)
    print_matriz(rotate_inplace(matriz))
