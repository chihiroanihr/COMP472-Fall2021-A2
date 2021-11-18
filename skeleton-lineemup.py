# We'll use the time module to measure the time of evaluating
# game tree in every move. It's a nice way to show the
# distinction between the basic Minimax and Minimax with
# alpha-beta pruning :)
import time
from input_functions import *

class Game:

    # Constants
    MINIMAX = 0
    ALPHABETA = 1
    HUMAN = 2
    AI = 3
    
    def __init__(self, size_board, number_blocks, position_blocks, size_lineup, max_depth_X, max_depth_O, max_time, recommend=True):
        self.size_board = size_board
        self.number_blocks = number_blocks
        self.position_blocks = position_blocks
        self.size_lineup = size_lineup
        self.recommend = recommend
        self.max_depth_X = max_depth_X
        self.max_depth_O = max_depth_O
        self.max_time = max_time
        self.initialize_game()
        
    def initialize_game(self):
        # initialize current state matrix with '.' 
        self.current_state = [['.' for x in range(self.size_board)] for y in range(self.size_board)] 

        # add blocks to the current state (modify '.' to blocks)
        for block in self.position_blocks:
            x = block[0]
            y = block[1]
            # The x-axis is the horizontal row, and the y-axis is the vertical column.
            self.current_state[y][x] = '*'

		# Player X always plays first
        self.player_turn = 'X'
    
    def draw_board(self, count_move=False):
        # print Horizontal categories
        ch = 'A'
        print('  ', end="")
        for index in range(self.size_board):
            print(ch, end="")
            ch = chr(ord(ch) + 1)
        if count_move: # output count moves if game has started
            print("  (move #" + str(count_move), ")", end="")
        print()

        # print horizontal line
        print(' +', end="")
        print('-' * self.size_board)
        
        # print current state
        for y in range(self.size_board):
            print(str(y) + '|', end="")
            for x in range(self.size_board):
                print(F'{self.current_state[x][y]}', end="")
            print()
        print()

        # output to file
        with open(self.filename, 'a') as f:
            f.write("\n")
            if (not count_move):
                f.write("Initial configuration of the board:\n")
            f.write('  ')
            ch = 'A'
            for index in range(self.size_board):
                f.write(ch)
                ch = chr(ord(ch) + 1)
            if count_move:
                f.write("  (move #" + str(count_move))
                f.write(")")
            f.write("\n")
            f.write(' +')
            f.write('-' * self.size_board)
            f.write("\n")
            for y in range(self.size_board):
                f.write(str(y) + '|')
                for x in range(self.size_board):
                    f.write(F'{self.current_state[x][y]}')
                f.write("\n")
            f.write("\n")


    # Determines if the made move is a legal move
    def is_valid(self, px, py):
        if px < 0 or px >= self.size_board or py < 0 or py >= self.size_board:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

	# Checks if the game has ended and returns the winner in each case
    def is_end(self):
		#### Vertical win ###
        for x in range(self.size_board):
            for y in range(self.size_board - self.size_lineup + 1):
                check_win = []
                for l in range(self.size_lineup):
                    check_win.append(self.current_state[y+l][x])
                if all(elem == check_win[0] for elem in check_win) and ('.' not in check_win) and ('*' not in check_win):
                    return self.current_state[y + l][x]
        #### Horizontal win ###
        for y in range(self.size_board):
            for i in range(self.size_board - self.size_lineup + 1):
                check_win = []
                for x in range(self.size_lineup):
                    check_win.append(self.current_state[y][x+i])
                if all(elem == check_win[0] for elem in check_win) and ('.' not in check_win) and ('*' not in check_win):
                    return self.current_state[y][x+i]
        #### Main diagonal win ###
        #  First Half
        i = 0
        while (i < self.size_board) :
            check_win = []
            j = i
            while (j >= 0 and i - j < self.size_board) :
                check_win.append(self.current_state[i - j][j])
                j -= 1
            for y in range(len(check_win) - self.size_lineup + 1):
                check_sub_win = []
                for x in range(self.size_lineup):
                    check_sub_win.append(check_win[x+y])
                if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= self.size_lineup and ('.' not in check_win) and ('*' not in check_win):
                    return check_sub_win[0]
            i += 1
        #  Second Half
        i = 1
        while (i < self.size_board) :
            check_win = []
            j = self.size_board - 1
            k = i
            while (j >= 0 and k < self.size_board) :
                check_win.append(self.current_state[k][j])
                j -= 1
                k += 1
            for y in range(len(check_win) - self.size_lineup + 1):
                check_sub_win = []
                for x in range(self.size_lineup):
                    check_sub_win.append(check_win[x+y])
                if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= self.size_lineup and ('.' not in check_win) and ('*' not in check_win):
                    return check_sub_win[0]
            i += 1
        #### Second diagonal win ###
        #  First Half
        i = 0
        while (i < self.size_board) :
            check_win = []
            k = i
            j = 0
            while (k >= 0 and j <= i) :
                check_win.append(self.current_state[self.size_board-1-k][j])
                j += 1
                k -= 1
            for y in range(len(check_win) - self.size_lineup + 1):
                check_sub_win = []
                for x in range(self.size_lineup):
                    check_sub_win.append(check_win[x+y])
                if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= self.size_lineup and ('.' not in check_win) and ('*' not in check_win):
                    return check_sub_win[0]
            i += 1
        #  Second Half
        i = 1
        while (i < self.size_board):
            check_win = []
            k = i
            j = 0
            while (k < self.size_board):
                check_win.append(self.current_state[j][k])
                j += 1
                k += 1
            for y in range(len(check_win) - self.size_lineup + 1):
                check_sub_win = []
                for x in range(self.size_lineup):
                    check_sub_win.append(check_win[x+y])
                if all(elem == check_sub_win[0] for elem in check_sub_win) and len(check_sub_win) >= self.size_lineup and ('.' not in check_win) and ('*' not in check_win):
                    return check_sub_win[0]
            i += 1
        #### Is whole board full? ###
        for y in range(self.size_board):
            for x in range(self.size_board):
                # There's an empty field, we continue the game
                if (self.current_state[y][x] == '.'):
                    return None
        #### It's a tie! ###
        return '.'

    def check_end(self):
        self.result = self.is_end()
        # TODO: Printing the appropriate message if the game has ended
        if self.result != None:
            if self.result == 'X':
                print('The winner is X!')
            elif self.result == 'O':
                print('The winner is O!')
            elif self.result == '.':
                print("It's a tie!")
            self.initialize_game()
        return self.result

    def input_move(self):
        ch = 'A'
        colm_dict = dict()
        for i in range(self.size_board):
            colm_dict[ch] = i
            ch = chr(ord(ch) + 1)
        while True:
            print(F'Player {self.player_turn}, enter your move:')
            try:
                px = input('Enter the x coordinate (in letter): ')
                py = int(input('Enter the y coordinate (in number): '))
            except ValueError:
                print("!!! You must enter integer value, try again !!!")
            if len(px) == 1 and px in colm_dict:
                px = colm_dict[px]
                if self.is_valid(px, py):
                    return (px,py)
            print('!!! This move is not valid! Try again !!!')

    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn

    def e1(self):
        num_X, num_O = 0, 0
        #### Horizontal evaluation ###
        for y in range(self.size_board):
            for x in range(self.size_board - self.size_lineup + 1):
                if all(self.current_state[y][x+i] == 'X' or self.current_state[y][x+i] == '.' for i in range(self.size_lineup)):
                    num_X += 1
                if all(self.current_state[y][x+i] == 'O' or self.current_state[y][x+i] == '.' for i in range(self.size_lineup)):
                    num_O += 1
        ### Vertical evaluation ###
        for y in range(self.size_board - self.size_lineup + 1):
            for x in range(self.size_board):
                if all(self.current_state[y+i][x] == 'X' or self.current_state[y+i][x] == '.' for i in range(self.size_lineup)):
                    num_X += 1
                if all(self.current_state[y+i][x] == 'O' or self.current_state[y+i][x] == '.' for i in range(self.size_lineup)):
                    num_O += 1
        ### Diagonal evalutation ###
        #  First Half
        i = 0
        while (i < self.size_board) :
            check_open = []
            j = i
            while (j >= 0 and i - j < self.size_board) :
                check_open.append(self.current_state[i - j][j])
                j -= 1
            for y in range(len(check_open) - self.size_lineup + 1):
                if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_X += 1
                if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_O += 1
            i += 1
        #  Second Half
        i = 1
        while (i < self.size_board) :
            check_open = []
            j = self.size_board - 1
            k = i
            while (j >= 0 and k < self.size_board) :
                check_open.append(self.current_state[k][j])
                j -= 1
                k += 1
            for y in range(len(check_open) - self.size_lineup + 1):
                if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_X += 1
                if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_O += 1
            i += 1
        #### Second diagonal evaluation ###
        i = 0
        while (i < self.size_board) :
            check_open = []
            k = i
            j = 0
            while (k >= 0 and j <= i) :
                check_open.append(self.current_state[self.size_board-1-k][j])
                j += 1
                k -= 1
            for y in range(len(check_open) - self.size_lineup + 1):
                if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_X += 1
                if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_O += 1
            i += 1
        #  Second Half
        i = 1
        while (i < self.size_board):
            check_open = []
            k = i
            j = 0
            while (k < self.size_board):
                check_open.append(self.current_state[j][k])
                j += 1
                k += 1
            for y in range(len(check_open) - self.size_lineup + 1):
                if all(check_open[x+y] == 'X' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_X += 1
                if all(check_open[x+y] == 'O' or check_open[x+y] == '.' for x in range(self.size_lineup)):
                    num_O += 1
            i += 1
        return num_X - num_O
    
    def e2(self):
        weight = 1
        weight_dict = dict()
        for i in range(self.size_lineup + 1):
            weight_dict[i] = weight
            weight *= 100
        num_X, num_O = 0, 0
        #### Horizontal evaluation ###
        for y in range(self.size_board):
            for x in range(self.size_board - self.size_lineup + 1):
                check_open = []
                for l in range(self.size_lineup):
                    check_open.append(self.current_state[y][x+l])
                if all(check_open[i] == 'X' or check_open[i] == '.' for i in range(self.size_lineup)):
                    count_X = check_open.count("X")
                    num_X += weight_dict[count_X]
                if all(check_open[i] == 'O' or check_open[i] == '.' for i in range(self.size_lineup)):
                    count_O = check_open.count("O")
                    num_O += weight_dict[count_O]
        ### Vertical evaluation ##
        for y in range(self.size_board - self.size_lineup + 1): 
            for x in range(self.size_board):
                check_open = []
                for l in range(self.size_lineup):
                    check_open.append(self.current_state[y+l][x])
                if all(check_open[i] == 'X' or check_open[i] == '.' for i in range(self.size_lineup)):
                    count_X = check_open.count("X")
                    num_X += weight_dict[count_X]
                if all(check_open[i] == 'O' or check_open[i] == '.' for i in range(self.size_lineup)):
                    count_O = check_open.count("O")
                    num_O += weight_dict[count_O]
        ### Diagonal evalutation ###
        #  First Half
        i = 0
        while (i < self.size_board) :
            check_open = []
            j = i
            while (j >= 0 and i - j < self.size_board) :
                check_open.append(self.current_state[i - j][j])
                j -= 1
            for y in range(len(check_open) - self.size_lineup + 1):
                check_sub_open = []
                for x in range(self.size_lineup):
                    check_sub_open.append(check_open[x+y])
                if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_X = check_sub_open.count("X")
                    num_X += weight_dict[count_X]
                if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_O = check_sub_open.count("O")
                    num_O += weight_dict[count_O]
            i += 1
        #  Second Half
        i = 1
        while (i < self.size_board) :
            check_open = []
            j = self.size_board - 1
            k = i
            while (j >= 0 and k < self.size_board) :
                check_open.append(self.current_state[k][j])
                j -= 1
                k += 1
            for y in range(len(check_open) - self.size_lineup + 1):
                check_sub_open = []
                for x in range(self.size_lineup):
                    check_sub_open.append(check_open[x+y])
                if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_X = check_sub_open.count("X")
                    num_X += weight_dict[count_X]
                if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_O = check_sub_open.count("O")
                    num_O += weight_dict[count_O]
            i += 1
        #### Second diagonal evaluation ###
        #  First Half
        i = 0
        while (i < self.size_board) :
            check_open = []
            k = i
            j = 0
            while (k >= 0 and j <= i) :
                check_open.append(self.current_state[self.size_board-1-k][j])
                j += 1
                k -= 1
            for y in range(len(check_open) - self.size_lineup + 1):
                check_sub_open = []
                for x in range(self.size_lineup):
                    check_sub_open.append(check_open[x+y])
                if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_X = check_sub_open.count("X")
                    num_X += weight_dict[count_X]
                if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_O = check_sub_open.count("O")
                    num_O += weight_dict[count_O]
            i += 1
        #  Second Half
        i = 1
        while (i < self.size_board):
            check_open = []
            k = i
            j = 0
            while (k < self.size_board):
                check_open.append(self.current_state[j][k])
                j += 1
                k += 1
            for y in range(len(check_open) - self.size_lineup + 1):
                check_sub_open = []
                for x in range(self.size_lineup):
                    check_sub_open.append(check_open[x+y])
                if all(check_sub_open[i] == 'X' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_X = check_sub_open.count("X")
                    num_X += weight_dict[count_X]
                if all(check_sub_open[i] == 'O' or check_sub_open[i] == '.' for i in range(self.size_lineup)):
                    count_O = check_sub_open.count("O")
                    num_O += weight_dict[count_O]
            i += 1
        return num_X - num_O


    def minimax(self, depth=0, max=False):
    	# Minimizing for 'X' and maximizing for 'O'

		# Possible values are:
		# -1 - win for 'X'
		# 0  - a tie
		# 1  - loss for 'X'

		# We're initially setting it to 2 or -2 as worse than the worst case:
        value = 1000000+1
        if max:
            value = -1000000-1

        x = None
        y = None
        
        # if self.isend(): return gamestate
        result = self.is_end()
        if result == 'X':
            return (-1000000, x, y)
        elif result == 'O':
            return (1000000, x, y)
        elif result == '.':
            return (0, x, y)

        # if max depth reached: return estimate(gamestate)
        if self.player_turn == 'X' and depth >= self.max_depth_X:
            if self.e_func_X == 1:
                return (self.e1(), x, y)
            else:
                return (self.e2(), x, y)
        elif self.player_turn == 'O' and depth >= self.max_depth_O:
            if self.e_func_O == 1:
                return (self.e1(), x, y)
            else:
                return (self.e2(), x, y)
        
        # if time is up: return estimate(gamestate)
        if (round(time.time() - self.start, 7) >= self.max_time):
            return (value, x, y)
        
        for i in range(self.size_board):
            for j in range(self.size_board):
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        # On the empty field player 'O' makes a move and calls Min
                        # That's one branch of the game tree.
                        (v, _, _) = self.minimax(depth+1, max=False)
                        # Fixing the maxv value if needed
                        if v > value:
                            value = v
                            x = i
                            y = j
                    else:
                        self.current_state[i][j] = 'X'
                        (v, _, _) = self.minimax(depth+1, max=True)
                        if v < value:
                            value = v
                            x = i
                            y = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'
        return (value, x, y)

    def alphabeta(self, depth=0, alpha=-1000000, beta=1000000, max=False):
        # Minimizing for 'X' and maximizing for 'O'
        # Possible values are:
        # -1 - win for 'X'
        # 0  - a tie
        # 1  - loss for 'X'
        # We're initially setting it to 1000000 or -1000000 as worse than the worst case:
        value = 1000000 + 1
        if max:
            value = -1000000-1

        x = None
        y = None

        result = self.is_end()
        if result == 'X':
            return (-1000000, x, y)
        elif result == 'O':
            return (1000000, x, y)
        elif result == '.':
            return (0, x, y)

        # if max depth reached: return estimate(gamestate)
        if self.player_turn == 'X' and depth >= self.max_depth_X:
            return (self.e2(), x, y)
        elif self.player_turn == 'O' and depth >= self.max_depth_O:
            return (self.e1(), x, y)
        
        # if time is up: return estimate(gamestate)
        if (round(time.time() - self.start, 7) >= self.max_time):
            return (value, x, y)

        for i in range(self.size_board):
            for j in range(self.size_board):
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        (v, _, _) = self.alphabeta(depth+1, alpha, beta, max=False)
                        if v > value:
                            value = v
                            x = i
                            y = j
                    else:
                        self.current_state[i][j] = 'X'
                        (v, _, _) = self.alphabeta(depth+1, alpha, beta, max=True)
                        if v < value:
                            value = v
                            x = i
                            y = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'

                    if max:
                        if value >= beta:
                            return (value, x, y)
                        if value > alpha:
                            alpha = value
                    else:
                        if value <= alpha:
                            return (value, x, y)
                        if value < beta:
                            beta = value
        return (value, x, y)


    # let's make a game loop that allows us to play against the AI!
    def play(self, algo_X=1, algo_O=1, e_func_X=2, e_func_O=1, player_x=2, player_o=2):
        options = {0: self.MINIMAX, 1: self.ALPHABETA, 2: self.HUMAN, 3: self.AI}
        self.algo_X = options.get(algo_X)
        self.algo_O = options.get(algo_O)
        self.player_x = options.get(player_x)
        self.player_o = options.get(player_o)
        self.e_func_X = e_func_X
        self.e_func_O = e_func_O

        self.write_initial_config_to_file()

        count_move = 0
        x_letter_axis = [chr(ord('A')+num) for num in range(self.size_board)]

        while True:
            self.draw_board(count_move)
            count_move += 1
            if self.check_end():
                return

            start = time.time()
            self.start = start

            if self.player_turn == 'X' and self.algo_X == self.MINIMAX:
                (_, x, y) = self.minimax(max=False)
                #print("X player, MINIMAX ", x, y)
            elif self.player_turn == 'O' and self.algo_O == self.MINIMAX:
                (_, x, y) = self.minimax(max=True)
                #print("O player, MINIMAX ", x, y)    
            elif self.player_turn == 'X' and self.algo_X == self.ALPHABETA:
                (m, x, y) = self.alphabeta(max=False)
                #print("X player, alphabeta ", m, x, y)
            else: #self.player_turn == 'O' and self.algo_O == self.ALPHABETA:
                (m, x, y) = self.alphabeta(max=True)
                #print("O player, alphabeta ", m, x, y)

            end = time.time()
            
            with open(self.filename, "a") as f:
                if (self.player_turn == 'X' and self.player_x == self.HUMAN) or (self.player_turn == 'O' and self.player_o == self.HUMAN):
                    if self.recommend:
                        print(F'Evaluation time: {round(end - start, 7)}s')
                        print(F'Recommended move: x = {x_letter_axis[x]}, y = {y}')
                        f.write(F'Evaluation time: {round(end - start, 7)}s\n')
                        f.write(F'Recommended move: x = {x_letter_axis[x]}, y = {y}\n')
                    print()
                    (x,y) = self.input_move()
                    print(F'Player {self.player_turn} under HUMAN control plays: {x_letter_axis[x]}{y}')
                    f.write(F'Player {self.player_turn} under HUMAN control plays: {x_letter_axis[x]}{y}\n')
                    print()
                if (self.player_turn == 'X' and self.player_x == self.AI) or (self.player_turn == 'O' and self.player_o == self.AI):
                    print(F'Player {self.player_turn} under AI control plays: {x_letter_axis[x]}{y}')
                    print(F'Evaluation time: {round(end - start, 7)}s')
                    print()
                    f.write(F'Player {self.player_turn} under AI control plays: {x_letter_axis[x]}{y}\n')
                    f.write(F'Evaluation time: {round(end - start, 7)}s')
            self.current_state[x][y] = self.player_turn
            self.switch_player()
            print()

    def write_initial_config_to_file(self):
        self.filename = "gameTrace-" + str(self.size_board) + str(self.number_blocks) + str(self.size_lineup) + str(self.max_time) + ".txt"
        with open(self.filename, "w") as f:
            f.write("[The parameters of the game]\n(n: size of board, b: number of blocks, s: size of winning lineup, t: maximum time allowed):")
            f.write("\n\tn = " + str(self.size_board))
            f.write("\n\tb = " + str(self.number_blocks))
            f.write("\n\ts = " + str(self.size_lineup))
            f.write("\n\tt = " + str(self.max_time))
            
            f.write("\n\n[Position of the blocks]")
            if self.number_blocks != 0:
                for block in self.position_blocks:
                    x = block[0]
                    y = block[1]
                    f.write("\n\t(" + str(x) + ", " + str(y) + ")")
            else:
                f.write("!!! There are no blocks in this game !!!")
            
            f.write("\n\n[Parameters of each player]")
            f.write("\n\tPlayer X: ")
            if self.player_x == 2:
                f.write("HUMAN")
            else:
                f.write("AI")
            f.write("\n\tPlayer O: ")
            if self.player_o == 2:
                f.write("HUMAN")
            else:
                f.write("AI")

            if self.player_x == 3:
                f.write("\n\nPlayer X:")
                f.write("AI")
                f.write("\n\tMaximum depth = " + str(self.max_depth_X))
                if (self.algo_X == 0):
                    f.write("\n\tAdversarial type = Minmax")
                else:
                    f.write("\n\tAdversarial type = Alphabeta")
                if (self.e_func_X == 1):
                        f.write("\n\tEuristic func = e1 (simple function)")
                else:
                    f.write("\n\tEuristic func = e2 (complex function)")
            if self.player_o == 3:
                f.write("\n\nPlayer O")
                f.write("AI")
                f.write("\n\tMaximum depth = " + str(self.max_depth_O))
                if (self.algo_O == 0):
                    f.write("\n\tAdversarial type = Minmax")
                else:
                    f.write("\n\tAdversarial type = Alphabeta")
                if (self.e_func_O == 1):
                    f.write("\n\tEuristic func = e1(regular)")
                else:
                    f.write("\n\tEuristic func = e2(defensive)")
            f.write("\n\n")


def main():
    '''
    # settings/parameters for creating game board
    size_board = input_get_size_board()
    number_blocks = input_get_number_blocks(size_board)
    position_blocks = input_get_position_blocks(number_blocks, size_board)
    size_lineup = input_get_size_lineup(size_board)

    # settings/parameters when game starts/play
    max_depth1, max_depth2 = input_get_max_depth()
    max_time = input_get_max_time()
    '''

    size_board = 5
    number_blocks = 2
    position_blocks = set(((2, 3), (0, 2)))
    size_lineup = 3

    max_depth_X = 5
    max_depth_O = 3
    max_time = 5

    play_mode1, play_mode2 = input_get_play_mode()
    adversarial_type_X, adversarial_type_O = input_get_adversarial_type()
    heuristic_func_X, heuristic_func_O = input_get_heuristic_func()

    print("\n\n\n --------------\n[ Game Started ]\n --------------\n")
    g = Game(size_board, number_blocks, position_blocks, size_lineup, max_depth_X, max_depth_O, max_time, recommend=True)
    g.play(algo_X=adversarial_type_X, algo_O=adversarial_type_O, e_func_X=heuristic_func_X, e_func_O=heuristic_func_O, player_x=play_mode1, player_o=play_mode2)
    #g.play(algo_X=adversarial_type[0], algo_O=adversarial_type[1], e_func_X=heuristic_func_X, e_func_O=heuristic_func_O, player_x=play_mode1, player_o=play_mode2)

if __name__ == "__main__":
	main()