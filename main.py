from utils import generate_board, update_prob_distribution, get_position, get_choice, get_number_of_moves
from transition_matrix import generate_transition_matrix
from game import Dice
import numpy as np

def get_probability(N: int, TM: np.array) -> None:
    start = get_position(N, 'starting')
    end = get_position(N, 'ending')
    moves = get_number_of_moves()

    # P(Start i, End j, in m moves = (TM^m)[i][j])
    temp_mtrx = np.linalg.matrix_power(TM, moves)

    print(f'The probability of going from square {start} to {end} in {moves} moves is {temp_mtrx[start][end]:.3g}.')

    return

def main() -> None:
    board, sides = generate_board('input.txt')
    N = board.size
    dice = Dice(sides)
    print(f'The {sides} sided dice, by default, has a uniform probability distibution.')

    # Choose whether to update the probability distribution.
    choice = get_choice('Would you like to modify the probability distribution? [Y/N]: ')

    if choice.upper() == 'Y':
        update_prob_distribution(dice)

    TM = generate_transition_matrix(dice, board)

    while True:
        # Choose whether to continue seeing probability
        choice = get_choice('Would you like to continue finding out probabilities? [Y/N]: ')

        if choice.upper() == 'N':
            break
        else:
            get_probability(N, TM)

if __name__ == '__main__':
    main()