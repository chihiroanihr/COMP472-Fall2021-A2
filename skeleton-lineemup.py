# We'll use the time module to measure the time of evaluating
# game tree in every move. It's a nice way to show the
# distinction between the basic Minimax and Minimax with
# alpha-beta pruning :)
import time
from input_functions import *

class Game:
    MINIMAX = 0
    ALPHABETA = 1
    HUMAN = 2
    AI = 3
    
    def __init__(self, size_board, number_blocks, position_blocks, size_lineup, recommend=True):
        self.initialize_game()
        self.size_board = size_board
        self.number_blocks = number_blocks
        self.position_blocks = position_blocks
        self.size_lineup = size_lineup
        self.recommend = recommend
    
    def initialize_game(self):
        self.current_state = [['.','.','.'],
							  ['.','.','.'],
							  ['.','.','.']]
		# Player X always plays first
        self.player_turn = 'X'
    
    def draw_board(self):
        print()
        for y in range(0, 3):
            for x in range(0, 3):
                print(F'{self.current_state[x][y]}', end="")
            print()
        print()




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
    play_mode = input_get_play_mode()
    
    g = Game(size_board, number_blocks, position_blocks, size_lineup, recommend=True)
    g.play(algo=Game.ALPHABETA,player_x=Game.AI,player_o=Game.AI)
    g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.HUMAN)

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