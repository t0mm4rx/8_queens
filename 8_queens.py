def is_ok(x1, y1, x2, y2):
    if (x1 == x2 or y1 == y2):
        return False
    if (abs(x2 - x1) == abs(y2 - y1)):
        return False
    return True

def is_array_ok(arr):
    for i in arr:
        for  j in arr:
            if (not i == j):
                if (not is_ok(i[0], i[1], j[0], j[1])):
                    return False
    return True

def print_grid(arr):
    for j in range(8):
        for i in range(8):
            if ([i, j] in arr):
                print("X ", end="")
            else:
                print("0 ", end="")
        print("\n", end="")

def get_potentials(arr):
    res = []
    for i in range(8):
        for j in range(8):
            if (not [i, j] in arr):
                cpy = arr.copy()
                cpy.append([i, j])
                if (is_array_ok(cpy)):
                    res.append([i, j])
    return res

def search(board):
    if (not is_array_ok(board)):
        return False
    if (len(board) >= 8):
        print("Solution found :")
        print_grid(board)
    for test in get_potentials(board):
        copy = board.copy()
        copy.append(test)
        search(copy)

arr = []
#print(get_potentials(arr))
#print(is_array_ok(arr))
#print_grid(arr)
search(arr)
