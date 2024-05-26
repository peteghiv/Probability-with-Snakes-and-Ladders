import numpy as np
from game import Game, Dice
from utils import get_new_square

def generate_transition_matrix(dice: Dice, board: Game) -> np.array:
    '''
    Generates the Transition Matrix for a given case
    of a Snakes and Ladders board.

    Args:
        - dice  : A dice object representing the dice used.
        - board : A Game object representing the board.
    
    Return Vals:
        - TM    : A numpy array of the Transition Matrix
                  for the given board.
    '''

    N = board.size

    # Initialise the Transition Matrix (TM) to contain all zeroes first.
    # Use (N+1) x (N+1) so that indexing is easier
    TM = np.zeros((N+1,N+1))

    '''
    Remark: Indexing of the TM is as follows:
        TM[i][j] = P(Start at Square(i), End at Square(j) in the next move)
    '''

    # Fill out the transition matrix when the player starts at square 0, 1, 2, ..., N-1
    for start_square in range(N):
        for roll in range(dice.sides):
            destination_square = get_new_square(N, start_square, roll+1, board) # account for roll being 0-indexed
            
            # Add the probability of this dice roll to the transition matrix.
            TM[start_square][destination_square] += dice.pdist[roll]

    # Finally account for starting at square N.
    # Once the player reaches the end of the board, it is taken that
    # they will remain there
    TM[N][N] = 1

    return TM