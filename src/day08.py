def create_layers(data, dim_x, dim_y):
    layers = []
    index = 0
    while True:
        lay = [[ 0 for x in range(dim_y)] for y in range(dim_x)]
        for x in range(dim_x):
            for y in range(dim_y):
                if index >= len(data):
                    return layers
                lay[x][y] = data[index]
                index += 1
        layers.append(lay)


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j)
        print()


def get_digit(matrix, digit):
    count = 0
    for j in matrix:
        count += j.count(digit)
    return count

def iter_matrix(mat):
    count1, count2 = 0, 0
    for i in mat:
        tmp = get_digit(i, 0)
        if tmp == 5:
            count1 = get_digit(i, 1)
            count2 = get_digit(i, 2)
    return (count1 * count2)


def decode_matrix(matrixes, dim_x, dim_y) :
    matrix = [[2 for _ in range(dim_y)] for _ in range(dim_x)]
    for mat in matrixes:
        for y in range(dim_y):
            for x in range(dim_x):
                if matrix[x][y] == 2 :
                    matrix[x][y] = mat[x][y]
    print_matrix([matrix])


with open("../data/day08.txt") as f:
    data = list(map(int, f.readline()))
    mat = create_layers(data, 6, 25)
    print(iter_matrix(mat))
    decode_matrix(mat,6,25)