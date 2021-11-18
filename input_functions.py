from random import randint

#####   INPUT FUNCITONS   #####
def input_get_size_board():
    while True:
        try:
            size_board = int(input('Enter the size of the board (range of input: 3 ~ 10): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if size_board < 3 or size_board > 10:
            print("!!! Invalid number, try again !!!")
            continue
        return size_board

def input_get_number_blocks(size_board):
    while True:
        try:
            number_blocks = int(input('Enter the number of blocks (range of input: 0 ~ ' + str(2*(size_board)) + '): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if number_blocks < 0 or number_blocks > 2*size_board:
            print("!!! Invalid number, try again !!!")
            continue
        return number_blocks

def generate_custom_coordinates(number_blocks, size_board, position_blocks):
    i = 1
    while (i <= number_blocks):
        try: 
            cord = input('Enter ' + str(i) + 'th block\'s coordinate separated by comma (ex: 1, 3)'
            + '\n(The size of board is ' + str(size_board) + ', thus the input should be <= ' + str(size_board) + '): ')
            cord = tuple(map(int, cord.split(', ')))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if any(c is None for c in cord) or any(c > size_board-1 for c in cord) or len(cord) == 1:
            print("!!! Invalid value, try again !!!")
            continue
        else:
            size_position_blocks = len(position_blocks)
            position_blocks.add(cord)
            if (len(position_blocks) == size_position_blocks): # size does not change after added --> duplicates added, try again
                print('!!! Duplicated coordinate has been added, try again !!!')
                continue
            else:
                i += 1
    return position_blocks
def random_position_blocks(number_blocks, size_board):
    # generate random UNIQUE blocks (to avoid duplicate coordinates)
    position_blocks = set()
    while len(position_blocks) < number_blocks:
        x, y = randint(0, size_board-1), randint(0, size_board-1)
        position_blocks.add((x, y))
    return position_blocks
def input_get_position_blocks(number_blocks, size_board):
    while True:
        try:
            choice = int(input('Enter the position of the blocks: '
            + '\n\t(1) Randomly Generate the block positions'
            + '\n\t(2) Manually enter the block positions in coordinates (ex: (3, 2), (2, 1))'
            + '\n(Enter 1 or 2): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if choice == 1: # if generate random
            position_blocks = random_position_blocks(number_blocks, size_board)
        elif choice == 2:
            position_blocks = generate_custom_coordinates(number_blocks, size_board, position_blocks)
            break
        else:
            print("!!! Invalid choice, try again !!!")
            continue  
    return position_blocks

def input_get_size_lineup(size_board):
    while True:
        try:
            size_lineup = int(input('Enter the winning line up size (range of input: 3 ~ ' + str(size_board) + '): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if size_lineup < 3 or size_lineup > size_board:
            print("!!! Invalid number, try again !!!")
            continue
        return size_lineup

def input_get_max_depth():
    while True:
        try:
            max_depth = input('Enter maximum depth of the adversarial search for player 1 and player 2 separated by comma (ex. 3, 6): ')
            max_depth = tuple(map(int, max_depth.split(', ')))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if any(m is None for m in max_depth) or len(max_depth) == 1:
            print("!!! Invalid value, try again !!!")
            continue
        return max_depth[0], max_depth[1]

def input_get_max_time():
    while True:
        try:
            max_time = int(input('Enter the maximum allowed time for your adversarial search to return a move (in seconds): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        return max_time

def input_get_play_mode():
    HUMAN = 2
    AI = 3
    while True:
        try:
            choice = int(input('Playmode: '
        + '\n\t(1) [Player X] Human  VS   [Player O] Human'
        + '\n\t(2) [Player X] Human  VS   [Player O] AI'
        + '\n\t(3) [Player X] AI     VS   [Playe O] Human'
        + '\n\t(4) [Player X] AI     VS   [Playe O] AI'
        + '\n(Enter 1, 2, 3, or 4): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if choice == 1:
            return HUMAN, HUMAN
        elif choice == 2:
            return HUMAN, AI
        elif choice == 3:
            return AI, HUMAN
        elif choice == 4:
            return AI, AI
        else:
            print("!!! Invalid choice, try again !!!")
            continue

def input_get_adversarial_type():
    MINIMAX = 0
    ALPHABETA = 1
    while True:
        try:
            print("Adversarial type available:\n\t(1) Minmax\n\t(2) Alphabeta")
            choice1 = int(input("Choose adversarial type of Player X to use (Enter 1 or 2): "))
            choice2 = int(input("Choose adversarial type of Player O to use (Enter 1 or 2): "))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if choice1 == 1 and choice2 == 1:
            return (MINIMAX, MINIMAX)
        elif choice1 == 1 and choice2 == 2:
            return (MINIMAX, ALPHABETA)
        elif choice1 == 2 and choice2 == 1:
            return (ALPHABETA, MINIMAX)
        elif choice1 == 2 and choice2 == 2:
            return (ALPHABETA, ALPHABETA)
        else:
            print("!!! Invalid choice, try again !!!")
            continue

def input_get_heuristic_func():
    while True:
        try:
            print("Heuristic functions available:\n\tE1: simple yet less accurate function\n\tE2: complex and time consuming yet more precise function")
            choice1 = int(input("Choose heuristic function of Player X to use (Enter 1 or 2): "))
            choice2 = int(input("Choose heuristic function of Player O to use (Enter 1 or 2): "))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if choice1 == 1 and choice2 == 1:
            return (1, 1)
        elif choice1 == 1 and choice2 == 2:
            return (1, 2)
        elif choice1 == 2 and choice2 == 1:
            return (2, 1)
        elif choice1 == 2 and choice2 == 2:
            return (2, 2)
        else:
            print("!!! Invalid choice, try again !!!")
            continue