'''
ls = ["X", "*", "X", "X", "X"]
size = len(ls)
lineup = 3
target = ['X']*3

print(any(ls[i] == ls[i+1] == ls[i+2] for i in range(size-2)))
'''

'''
ls = [["X", "*", "X", "X", "X"], ["*", ".", ".", ".", "X"], ["*", ".", ".", ".", "X"], ["*", ".", ".", ".", "X"], ["*", ".", ".", ".", "X"]]
size = len(ls)
lineup = 3
target = ['X']*3

print("start")
for y in range(len(ls)):
    for i in range(len(ls[y])-lineup+1):
        check_valid = []
        for j in range(lineup):
            print("Y, X ",str(y), str(j+i), end="  ")
            print(ls[y][j+i])
            check_valid.append(ls[y][j+i])
        print(all(elem == check_valid[0] for elem in check_valid) and ('.' not in check_valid))


size_board = 5
current_state = [['.' for x in range(size_board)] for y in range(size_board)] 
print(len(current_state))
'''

size_board = 5
size_lineup = 3
current_state = [["X", "*", "X", "X", "X"], 
["*", ".", "O", "O", "O"], 
["*", ".", "O", ".", "X"], 
["*", ".", "*", ".", "X"], 
["*", ".", ".", ".", "X"]]
# HORIZONTAL CHECK
print("===== HORIZONTAL CHECK ====")
for x in range(size_board):
    for y in range(size_board - size_lineup + 1):
        check_open = []
        for l in range(size_lineup):
            print("Y, X: ", y+l, x)
            check_open.append(current_state[y + l][x])
        if all(elem == check_open[0] for elem in check_open) and ('.' not in check_open) and ('*' not in check_open):
            print(check_open)
            print(current_state[y + l][x])
print()
print()
current_state = [
    ["X", "*", "X", "X", "X"], 
    ["*", ".", "O", "X", "O"], 
    ["*", "*", "O", ".", "X"], 
    ["*", "O", "*", ".", "X"], 
    ["O", ".", ".", ".", "X"]
    ]
print("===== MAIN DIAGONAL CHECK ====")
row = size_board
col = size_board
#  First Half
i = 0
while (i < size_board) :
    check_open = []
    j = i
    while (j >= 0 and i - j < size_board) :
        #  Display element value
        print(current_state[i - j][j], end ="  ")
        check_open.append(current_state[i - j][j])
        j -= 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(elem == check_sub_open[0] for elem in check_sub_open) and len(check_sub_open) >= size_lineup and ('.' not in check_open) and ('*' not in check_open):
            print(check_sub_open, end=" ")
            break
    i += 1
    print()
#  Second Half
i = 1
while (i < size_board) :
    check_open = []
    j = size_board - 1
    k = i
    while (j >= 0 and k < size_board) :
        #  Display element value
        print(current_state[k][j], end ="  ")
        check_open.append(current_state[k][j])
        j -= 1
        k += 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(elem == check_sub_open[0] for elem in check_sub_open) and len(check_sub_open) >= size_lineup and ('.' not in check_open) and ('*' not in check_open):
            print(check_sub_open, end=" ")
            break
    i += 1
    print()
print()
print()
print("===== SECOND DIAGONAL CHECK ====")
i = 0
while (i < size_board) :
    check_open = []
    k = i
    j = 0
    while (k >= 0 and j <= i) :
        #  Display element value
        print(current_state[size_board-1-k][j], end ="  ")
        check_open.append(current_state[size_board-1-k][j])
        j += 1
        k -= 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(elem == check_sub_open[0] for elem in check_sub_open) and len(check_sub_open) >= size_lineup and ('.' not in check_open) and ('*' not in check_open):
            print(check_sub_open, end=" ")
            break
    i += 1
    print()
i = 1
while (i < size_board):
    check_open = []
    k = i
    j = 0
    while (k < size_board):
        print(current_state[j][k], end ="  ")
        check_open.append(current_state[j][k])
        j += 1
        k += 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(elem == check_sub_open[0] for elem in check_sub_open) and len(check_sub_open) >= size_lineup and ('.' not in check_open) and ('*' not in check_open):
            print(check_sub_open, end=" ")
            break
    i += 1
    print()

print("\n\n")
current_state = [
    ["X", "*", "X", "X", "X"], 
    ["*", ".", "O", "X", "O"], 
    ["*", "*", "O", ".", "X"], 
    ["*", "O", "*", ".", "X"], 
    ["O", ".", ".", ".", "X"]
    ]
current_state = [
    [".", ".", ".", "."],
    ["O", "O", "X", "O"],
    [".", "X", ".", "."],
    [".", "X", ".", "."]
]
size_lineup = 3
size_board = len(current_state)

num_X, num_O = 0, 0
for y in range(size_board):
    for x in range(size_board - size_lineup + 1):
        if all(current_state[y][x+i] == 'X' or current_state[y][x+i] == '.' for i in range(size_lineup)):
            num_X += 1
        if all(current_state[y][x+i] == 'O' or current_state[y][x+i] == '.' for i in range(size_lineup)):
            num_O += 1
print("Horizontal", str(num_X), str(num_O))

num_X, num_O = 0, 0
for y in range(size_board - size_lineup + 1):
    for x in range(size_board):
        if all(current_state[y+i][x] == 'X' or current_state[y+i][x] == '.' for i in range(size_lineup)):
            num_X += 1
        if all(current_state[y+i][x] == 'O' or current_state[y+i][x] == '.' for i in range(size_lineup)):
            num_O += 1
print("Vertical", str(num_X), str(num_O))

num_X, num_O = 0, 0
#  First Half
i = 0
while (i < size_board) :
    check_open = []
    j = i
    while (j >= 0 and i - j < size_board) :
        check_open.append(current_state[i - j][j])
        j -= 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_X += 1
        if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_O += 1
    i += 1
#  Second Half
i = 1
while (i < size_board) :
    check_open = []
    j = size_board - 1
    k = i
    while (j >= 0 and k < size_board) :
        check_open.append(current_state[k][j])
        j -= 1
        k += 1
    for y in range(len(check_open) - size_lineup + 1):
        if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_X += 1
        if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_O += 1
    i += 1
print("Diagonal", str(num_X), str(num_O))

num_X, num_O = 0, 0
#  First Half
i = 0
while (i < size_board):
    check_open = []
    k = i
    j = 0
    while (k >= 0 and j <= i) :
        check_open.append(current_state[size_board-1-k][j])
        j += 1
        k -= 1
    for y in range(len(check_open) - size_lineup + 1):
        if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_X += 1
        if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_O += 1
    i += 1
#  Second Half
i = 1
while (i < size_board):
    check_open = []
    k = i
    j = 0
    while (k < size_board):
        check_open.append(current_state[j][k])
        j += 1
        k += 1
    for y in range(len(check_open) - size_lineup + 1):
        if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_X += 1
        if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(size_lineup)):
            num_O += 1
    i += 1
print("Second Diagonal", str(num_X), str(num_O))


print("\n\n")
current_state = [
    [".", ".", ".", "."],
    ["O", "O", "X", "O"],
    [".", "X", ".", "."],
    [".", "X", ".", "."]
]
weight = 1
weight_dict = dict()
for i in range(size_lineup):
    weight_dict[i] = weight
    weight *= 100

num_X, num_O = 0, 0
#### Horizontal evaluation ###
for y in range(size_board):
    for x in range(size_board - size_lineup + 1):
        check_open = []
        for l in range(size_lineup):
            check_open.append(current_state[y][x+l])
        if all(check_open[i] == 'X' or check_open[i] == '.' for i in range(size_lineup)):
            count_X = check_open.count("X")
            num_X += weight_dict[count_X]
        if all(check_open[i] == 'O' or check_open[i] == '.' for i in range(size_lineup)):
            count_O = check_open.count("O")
            num_O += weight_dict[count_O]
print("Horizontal", str(num_X), str(num_O))

### Vertical evaluation ###
num_X, num_O = 0, 0
for y in range(size_board - size_lineup + 1): 
    for x in range(size_board):
        check_open = []
        for l in range(size_lineup):
            check_open.append(current_state[y+l][x])
        if all(check_open[i] == 'X' or check_open[i] == '.' for i in range(size_lineup)):
            count_X = check_open.count("X")
            num_X += weight_dict[count_X]
        if all(check_open[i] == 'O' or check_open[i] == '.' for i in range(size_lineup)):
            count_O = check_open.count("O")
            num_O += weight_dict[count_O]
print("Vertical", str(num_X), str(num_O))

### Diagonal evalutation ###
num_X, num_O = 0, 0
#  First Half
i = 0
while (i < size_board) :
    check_open = []
    j = i
    while (j >= 0 and i - j < size_board) :
        check_open.append(current_state[i - j][j])
        j -= 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_X = check_sub_open.count("X")
            num_X += weight_dict[count_X]
        if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_O = check_sub_open.count("O")
            num_O += weight_dict[count_O]
    i += 1
#  Second Half
i = 1
while (i < size_board) :
    check_open = []
    j = size_board - 1
    k = i
    while (j >= 0 and k < size_board) :
        check_open.append(current_state[k][j])
        j -= 1
        k += 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_X = check_sub_open.count("X")
            num_X += weight_dict[count_X]
        if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_O = check_sub_open.count("O")
            num_O += weight_dict[count_O]
    i += 1
print("Diagonal", str(num_X), str(num_O))

#### Second diagonal win ###
num_X, num_O = 0, 0
#  First Half
i = 0
while (i < size_board) :
    check_open = []
    k = i
    j = 0
    while (k >= 0 and j <= i) :
        check_open.append(current_state[size_board-1-k][j])
        j += 1
        k -= 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_X = check_sub_open.count("X")
            num_X += weight_dict[count_X]
        if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_O = check_sub_open.count("O")
            num_O += weight_dict[count_O]
    i += 1
#  Second Half
i = 1
while (i < size_board):
    check_open = []
    k = i
    j = 0
    while (k < size_board):
        check_open.append(current_state[j][k])
        j += 1
        k += 1
    for y in range(len(check_open) - size_lineup + 1):
        check_sub_open = []
        for x in range(size_lineup):
            check_sub_open.append(check_open[x+y])
        if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_X = check_sub_open.count("X")
            num_X += weight_dict[count_X]
        if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(size_lineup)):
            count_O = check_sub_open.count("O")
            num_O += weight_dict[count_O]
    i += 1
print("Second Diagonal", str(num_X), str(num_O))