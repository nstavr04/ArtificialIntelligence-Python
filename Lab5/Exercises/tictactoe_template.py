def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    
    if (utility_of(state) != 0 or (state.count('X') + state.count('O')) == 9):
        return True

    return False

def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    if ((state[0] == 'X' and state[1] == 'X' and state[2] == 'X') or 
        (state[3] == 'X' and state[4] == 'X' and state[5] == 'X') or
        (state[6] == 'X' and state[7] == 'X' and state[8] == 'X') or
        (state[0] == 'X' and state[3] == 'X' and state[6] == 'X') or
        (state[1] == 'X' and state[4] == 'X' and state[7] == 'X') or
        (state[2] == 'X' and state[5] == 'X' and state[8] == 'X') or
        (state[0] == 'X' and state[4] == 'X' and state[8] == 'X') or
        (state[2] == 'X' and state[4] == 'X' and state[6] == 'X')):
            return 1
    elif ((state[0] == 'O' and state[1] == 'O' and state[2] == 'O') or
        (state[3] == 'O' and state[4] == 'O' and state[5] == 'O') or
        (state[6] == 'O' and state[7] == 'O' and state[8] == 'O') or
        (state[0] == 'O' and state[3] == 'O' and state[6] == 'O') or
        (state[1] == 'O' and state[4] == 'O' and state[7] == 'O') or
        (state[2] == 'O' and state[5] == 'O' and state[8] == 'O') or
        (state[0] == 'O' and state[4] == 'O' and state[8] == 'O') or
        (state[2] == 'O' and state[4] == 'O' and state[6] == 'O')):
            return -1
    else:
        return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    numX = state.count('X')
    numO = state.count('O')

    if numX >= numO:
        player = 'X'
    else:
        player = 'O'

    sucList = []
    singleList = []

    for i in state:
        # Every time we copy the state
        singleList = state.copy()

        if not (i == 'X' or i == 'O'):
            singleList[i] = player
            # appending to our results a tuple which containts the integer of the move played and the new state
            sucList.append((i, singleList))

    return sucList
     


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()