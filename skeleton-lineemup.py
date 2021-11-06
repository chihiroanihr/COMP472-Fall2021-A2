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
    
    def __init__(self, size_board, number_blocks, position_blocks, size_lineup, recommend=True):
        self.size_board = size_board
        self.number_blocks = number_blocks
        self.position_blocks = position_blocks
        self.size_lineup = size_lineup
        self.recommend = recommend
        self.initialize_game(size_board, position_blocks)
        self.draw_board(size_board)
        
    def initialize_game(self, size_board, position_blocks):
        # initialize current state matrix with '.' 
        self.current_state = [['.' for x in range(size_board)] for y in range(size_board)] 

        # add blocks to the current state (modify '.' to blocks)
        for cord in position_blocks:
            x = cord[0]
            y = cord[1]
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
            print("  move #" + str(count_move), end="")
        print()

        # print horizontal line
        print(' +', end="")
        print('-' * self.size_board)
        
        # print current state
        for y in range(self.size_board):
            print(str(y) + '|', end="")
            for x in range(self.size_board):
                print(F'{self.current_state[y][x]}', end="")
            print()
        print()

    # Determines if the made move is a legal move
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

	# Checks if the game has ended and returns the winner in each case
    def is_end(self):
		# Vertical win
        for x in range(self.size_board):
            for y in range(self.size_board - self.size_lineup + 1):
                check_win = []
                for l in range(self.size_lineup):
                    check_win.add(self.current_state[y + l][x])
                if all(check_win) and ('.' not in check_win):
                    return self.current_state[y + l][x]
        # Horizontal win
        for i in range(self.size_board):
            if (self.current_state[i] == ['X'] * self.size_lineup):
                return 'X'
            elif (self.current_state[i] == ['O'] * self.size_lineup):
                return 'O'
        # Main diagonal win
        for i in range(self.size_board - self.size_lineup + 1):
            check_win = []
            for l in range(self.size_lineup):
                check_win.add(self.current_state[i + l][i + l])
            if all(check_win) and ('.' not in check_win):
                return self.current_state[i + l][i + l]
        # Second diagonal win
        for i in range(self.size_board - self.size_lineup + 1):
            check_win = []
            for l in range(self.size_lineup):
                check_win.add(self.current_state[i + l][self.size_board-1 -i -l])
            if all(check_win) and ('.' not in check_win):
                return self.current_state[i + l][self.size_board-1 -i -l]
        # Is whole board full?
        for y in range(self.size_board):
            for x in range(self.size_board):
                # There's an empty field, we continue the game
                if (self.current_state[y][x] == '.'):
                    return None
        # It's a tie!
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
        while True:
            print(F'Player {self.player_turn}, enter your move:')
            px = int(input('enter the x coordinate: '))
            py = int(input('enter the y coordinate: '))
            if self.is_valid(px, py):
                return (px,py)
            else:
                print('The move is not valid! Try again.')

    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn


    # let's make a game loop that allows us to play against the AI!
    def play(self, algo=None, player_x=None, player_o=None):
        if algo == None:
            algo = self.ALPHABETA
        if player_x == None:
            player_x = self.HUMAN
        if player_o == None:
            player_o = self.HUMAN

        count_move = 1

        while True:
            self.draw_board(count_move)
            if self.check_end():
                return

            start = time.time()

            if algo == self.MINIMAX:
                if self.player_turn == 'X':
                    (_, x, y) = self.minimax(max=False)
                else:
                    (_, x, y) = self.minimax(max=True)
            else: # algo == self.ALPHABETA
                if self.player_turn == 'X':
                    (m, x, y) = self.alphabeta(max=False)
                else:
                    (m, x, y) = self.alphabeta(max=True)

            end = time.time()
            
            if (self.player_turn == 'X' and player_x == self.HUMAN) or (self.player_turn == 'O' and player_o == self.HUMAN):
                    if self.recommend:
                        print(F'Evaluation time: {round(end - start, 7)}s')
                        print(F'Recommended move: x = {x}, y = {y}')
                    (x,y) = self.input_move()
            if (self.player_turn == 'X' and player_x == self.AI) or (self.player_turn == 'O' and player_o == self.AI):
                        print(F'Evaluation time: {round(end - start, 7)}s')
                        print(F'Player {self.player_turn} under AI control plays: x = {x}, y = {y}')
            self.current_state[x][y] = self.player_turn
            self.switch_player()
'''
  ABCDE  (move #1)
 +-----
0|.....
1|.....
2|..X..
3|..*..
4|.....
'''



def main():
    # settings/parameters for creating game board
    size_board = input_get_size_board()
    number_blocks = input_get_number_blocks(size_board)
    position_blocks = input_get_position_blocks(number_blocks, size_board)
    size_lineup = input_get_size_lineup(size_board)

    # settings/parameters when game starts/play
    max_depth = input_get_max_depth()
    max_time = input_get_max_time()
    adversarial_type = input_get_adversarial_type()
    play_mode1, play_mode2 = input_get_play_mode()
    
    g = Game(size_board, number_blocks, position_blocks, size_lineup, recommend=True)
    g.play(algo=Game.adversarial_type, player_x=Game.play_mode1, player_o=Game.play_mode2)
    g.play(algo=Game.adversarial_type, player_x=Game.play_mode1,player_o=Game.play_mode2)

if __name__ == "__main__":
	main()


'''
Game Parameters:  Your program must accept the following game parameters.
(You do not need to check the validity of these input values; you can assume that they will be valid)
(a)  the size of the board –n– an integer in[3..10]
(b)  the number of blocs –b– an integer in[0..2n]
(c)  the positions of the blocs –b board coordinates
(d)  the winning line-up size –s– an integer in[3..n]
(e)  the maximum depth of the adversarial search for player 1 and for player 2 – 2 integers d1 and d2
(f)  the maximum allowed time (in seconds) for your program to return a move – t
    Your AI should not take more than t seconds to return its move.  If it does, your AI will automatically lose the game.  
    This entails that even if your adversarial search is allowed to go to a depth of d in the game tree, 
    it may not have time to do so every time.  Your program must monitor the time, 
    and if not enough time is left to explore all the states at depth d, 
    it must interrupt its search at depth d and return values for the remaining states quickly before time is up.
(g)  a Boolean to force the use of either minimax (FALSE) or alphabeta (TRUE) –a
(h)  the play modes Your program should be able to make either player be a human or the AI. 
    This means that you shouldbe able to run your program in all 4 combinations of players:  H-H, H-AI, AI-H and AI-AI.
'''