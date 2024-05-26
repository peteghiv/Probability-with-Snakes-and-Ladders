from game import Game, Dice

def generate_board(filepath: str = 'input.txt') -> tuple:
    '''
    Generates the Game object representing the board of
    the Snakes and Ladders game.

    Args:
        - path: The file path of the input text file
                representing the Snakes and Ladders
                board

    Return Vals: tuple(board, sides)
        - board: The Game object required.
        - sides: The number of sides on the dice
    '''

    # Get input from file and set up the Game object
    with open(filepath) as f:
        N, M, sides = [int(i) for i in f.readline().split(' ')]

        board = Game(N)
        
        for _ in range(M):
            start, end = [int(i) for i in f.readline().split(' ')]
            
            board.arr[start].modify_destination(end)

    return (board, sides)

def get_new_square(N: int, start_square: int, roll: int, board: Game) -> int:
    '''
    Gets the new square after a roll

    Args:
        - N                 : Size of the board
        - start_square      : The initial square the player is on
        - roll              : The number of steps required to take

    Return Vals:
        - The final square the player lands on
    '''
    cur_square = start_square

    # True  : Moving forwards
    # False : Moving backwards
    direction = True

    for _ in range(roll):
        # Edge Case 1: Currently at the end of the board, need to turn around
        if cur_square == N and direction:
            direction = False
        # Edge Case 2: Currently at the start of the board, need to turn around
        elif cur_square == 1 and not direction:
            direction = True

        # After considering edge cases, make the move
        if direction:
            cur_square += 1
        else:
            cur_square -= 1

    # We are now at the destination square, we now need to see if we require to
    # travel along a snake/ladder, or just stay there.
    return board.arr[cur_square].to

def get_choice(prompt: str) -> str:
    while True:
        choice = input(prompt)

        if choice.upper() not in ['Y', 'N']:
            print('Invalid Input.')
            continue
        else:
            return choice

def update_prob_distribution(dice: Dice) -> Dice:
    while True:
        temp = []

        for roll in range(dice.sides):
            temp.append(input(f'P(roll={roll+1}) = '))

        if dice.modify_distribution(temp):
            return dice
        else:
            choice = get_choice('Update failed. Continue? [Y/N]: ')

            if choice == 'Y':
                continue
            else:
                return dice

def get_position(N: int, start_or_end: str) -> int:
    while True:
        pos = input(f'Enter {start_or_end} square: ')

        if not pos.isdecimal():
            print(f'Error: Enter an integer from 0 (start of game) to {N}.')
            continue
        if not 0 <= int(pos) <= N:
            print(f'Error: Enter an integer from 0 (start of game) to {N}.')
            continue
        return int(pos)

def get_number_of_moves() -> int:
    while True:
        inp = input('Enter number of moves desired: ')

        if not inp.isdecimal():
            print('Invalid Input.')
            continue
        if int(inp) < 1:
            print('Invalid Input')
            continue

        return int(inp)