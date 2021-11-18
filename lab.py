from skeleton_lineemup import *

def main():
    total_games=[]
    game_config1=[]
    game_config2=[]
    total_average_evaluation_time = []
    total_num_states_evaluation = []
    total_average_evaluation_depth = []
    e2win = 0
    e1win = 0

    # Player X: e2, Player O: e1
    g1 = Game(7, 12, set(((5,6), (4,5), (5,0), (3,1), (5,1), (2,6), (5,5), (0,1), (5,4), (6,1), (3,6), (1,6))), 6, 4, 3, 4, recommend=True)
    g1.play(algo_X=1, algo_O=1, e_func_X=2, e_func_O=1, player_x=3, player_o=3)
    g2 = Game(7, 12, set(((5,6), (4,5), (5,0), (3,1), (5,1), (2,6), (5,5), (0,1), (5,4), (6,1), (3,6), (1,6))), 6, 4, 3, 4, recommend=True)
    g2.play(algo_X=1, algo_O=1, e_func_X=2, e_func_O=1, player_x=3, player_o=3)
    g3 = Game(7, 12, set(((5,6), (4,5), (5,0), (3,1), (5,1), (2,6), (5,5), (0,1), (5,4), (6,1), (3,6), (1,6))), 6, 4, 3, 4, recommend=True)
    g3.play(algo_X=1, algo_O=1, e_func_X=2, e_func_O=1, player_x=3, player_o=3)
    game_config1.append(g1)
    game_config1.append(g2)
    game_config1.append(g3)

    # Player X: e1, Player O: e2
    g4 = Game(7, 12, set(((5,6), (4,5), (5,0), (3,1), (5,1), (2,6), (5,5), (0,1), (5,4), (6,1), (3,6), (1,6))), 6, 4, 3, 4, recommend=True)
    g4.play(algo_X=1, algo_O=1, e_func_X=1, e_func_O=2, player_x=3, player_o=3)
    g5 = Game(7, 12, set(((5,6), (4,5), (5,0), (3,1), (5,1), (2,6), (5,5), (0,1), (5,4), (6,1), (3,6), (1,6))), 6, 4, 3, 4, recommend=True)
    g5.play(algo_X=1, algo_O=1, e_func_X=1, e_func_O=2, player_x=3, player_o=3)
    g6 = Game(7, 12, set(((5,6), (4,5), (5,0), (3,1), (5,1), (2,6), (5,5), (0,1), (5,4), (6,1), (3,6), (1,6))), 6, 4, 3, 4, recommend=True)
    g6.play(algo_X=1, algo_O=1, e_func_X=1, e_func_O=2, player_x=3, player_o=3)
    game_config2.append(g1)
    game_config2.append(g2)
    game_config2.append(g3)

    total_games.append(game_config1)
    total_games.append(game_config2)

    with open('scoreboard.txt', 'w') as f:
        for game in range(len(total_games)):
            for each_config in total_games[game]:
                size_board, number_blocks, size_lineup, max_depth_X, max_depth_O, max_time, algo_X, algo_O, result, e_func_X, e_func_O, average_e_time, num_states_evaluation, final_evaluation_by_depth, average_evaluation_depth, average_recursion_depth = each_config
                if game == 0 and result=='X':
                    e2win += 1
                elif game == 0 and result == 'O':
                    e1win += 1
                elif game == 1 and result == 'X':
                    e1win += 1
                elif game == 1 and result == 'O':
                    e2win += 1

                total_average_evaluation_time.append(average_e_time)
                total_num_states_evaluation.append(num_states_evaluation)
                total_average_evaluation_depth.append(average_evaluation_depth)

        f.write(F'n={size_board} b={number_blocks} s={size_lineup} t={max_time}\n\n')
        ad_x = (True if algo_X == 2 else False)
        ad_y = (True if algo_O == 2 else False)
        f.write(F'Player 1: d={max_depth_X} a={ad_x}\n')
        f.write(F'Player 2: d={max_depth_O} a={ad_y}\n')
        f.write('\n')

        f.write(str(len(total_games)) + ' games' + '\n')
        f.write('\n')
        f.write(F'Total wins for heuristic e1: ' + str(e1win) + ' (' + str(e1win / len(total_games*2) * 100) + ' (regular)\n')
        f.write(F'Total wins for heuristic e2: ' + str(e2win) + ' (' + str(e2win / len(total_games*2) * 100) + ' (defensive)\n')
        f.write('\n')
        f.write('i\tAverage evaluation time: ' + str(sum(total_average_evaluation_time)/len(total_average_evaluation_time)) + '\n')
        f.write('ii\tTotal heuristic evaluations: ' + str(sum(total_num_states_evaluation)/len(total_num_states_evaluation)) + '\n')
        f.write('Evaluations by depth: ' + str(final_evaluation_by_depth) + '\n')
        f.write('v\tAverage evaluation depth: ' + str(sum(total_average_evaluation_depth)/len(total_average_evaluation_depth)) + '\n')

if __name__ == "__main__":
	main()
