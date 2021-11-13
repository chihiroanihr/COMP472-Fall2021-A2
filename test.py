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
        check_win = []
        for l in range(size_lineup):
            print("Y, X: ", y+l, x)
            check_win.append(current_state[y + l][x])
        if all(elem == check_win[0] for elem in check_win) and ('.' not in check_win) and ('*' not in check_win):
            print(check_win)
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
    check_win = []
    j = i
    while (j >= 0 and i - j < size_board) :
        #  Display element value
        print(current_state[i - j][j], end ="  ")
        check_win.append(current_state[i - j][j])
        j -= 1
    for y in range(len(check_win) - size_lineup + 1):
        check_sub_win = []
        for x in range(size_lineup):
            check_sub_win.append(check_win[x+y])
        if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= size_lineup and ('.' not in check_win) and ('*' not in check_win):
            print(check_sub_win, end=" ")
            break
    i += 1
    print()
#  Second Half
i = 1
while (i < size_board) :
    check_win = []
    j = size_board - 1
    k = i
    while (j >= 0 and k < size_board) :
        #  Display element value
        print(current_state[k][j], end ="  ")
        check_win.append(current_state[k][j])
        j -= 1
        k += 1
    for y in range(len(check_win) - size_lineup + 1):
        check_sub_win = []
        for x in range(size_lineup):
            check_sub_win.append(check_win[x+y])
        if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= size_lineup and ('.' not in check_win) and ('*' not in check_win):
            print(check_sub_win, end=" ")
            break
    i += 1
    print()
print()
print()
print("===== SECOND DIAGONAL CHECK ====")
i = 0
while (i < size_board) :
    check_win = []
    k = i
    j = 0
    while (k >= 0 and j <= i) :
        #  Display element value
        print(current_state[size_board-1-k][j], end ="  ")
        check_win.append(current_state[size_board-1-k][j])
        j += 1
        k -= 1
    for y in range(len(check_win) - size_lineup + 1):
        check_sub_win = []
        for x in range(size_lineup):
            check_sub_win.append(check_win[x+y])
        if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= size_lineup and ('.' not in check_win) and ('*' not in check_win):
            print(check_sub_win, end=" ")
            break
    i += 1
    print()
i = 1
while (i < size_board):
    check_win = []
    k = i
    j = 0
    while (k < size_board):
        print(current_state[j][k], end ="  ")
        check_win.append(current_state[j][k])
        j += 1
        k += 1
    for y in range(len(check_win) - size_lineup + 1):
        check_sub_win = []
        for x in range(size_lineup):
            check_sub_win.append(check_win[x+y])
        if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= size_lineup and ('.' not in check_win) and ('*' not in check_win):
            print(check_sub_win, end=" ")
            break
    i += 1
    print()