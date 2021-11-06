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
        if any(c is None for c in cord) or all(c > size_board-1 for c in cord):
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
def input_get_position_blocks(number_blocks, size_board):
    while True:
        try:
            choice = int(input('Enter the position of the blocks: '
            + '\n\t(1) Manually enter the block positions in coordinates (ex: (3, 2), (2, 1))'
            + '\n\t(2) Randomly Generate the block positions'
            + '\n(Enter 1 or 2): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        position_blocks = set() # generate random UNIQUE blocks (to avoid duplicate coordinates)
        if choice == 2: # if generate random
            while len(position_blocks) < number_blocks:
                x, y = randint(0, size_board-1), randint(0, size_board-1)
                position_blocks.add((x, y))
            break
        elif choice == 1:
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
        if any(m is None for m in max_depth):
            print("!!! Invalid value, try again !!!")
            continue
        return max_depth

def input_get_max_time():
    while True:
        try:
            max_time = int(input('Enter the maximum allowed time for your adversarial search to return a move (in seconds): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        return max_time

def input_get_adversarial_type():
    while True:
        try:
            choice = int(input('Adversarial type: \n\t(1) minmax\n\t(2) alphabeta\n(Enter 1 or 2): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if choice!=1 and choice!=2:
            print("!!! Invalid choice, try again !!!")
            continue
        return choice

def input_get_play_mode():
    while True:
        try:
            choice = int(input('Playmode: '
        + '\n\t(1) [Player 1] Human  VS   [Player 2] Human'
        + '\n\t(2) [Player 1] Human  VS   [Player 2] AI'
        + '\n\t(3) [Player 1] AI     VS   [Playe 2] Human'
        + '\n\t(4) [Player 1] AI     VS   [Playe 2] AI'
        + '\n(Enter 1, 2, 3, or 4): '))
        except ValueError:
            print("!!! You must enter integer value, try again !!!")
            continue
        if choice!=1 and choice!=2 and choice!=3 and choice!=4:
            print("!!! Invalid choice, try again !!!")
            continue
        return choice