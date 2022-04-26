def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for s in successors_of(state):
            v = max(v, min_value(s))
        # print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for s in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    state = argmax(successors_of(state), lambda a: min_value(a))
    return state

def is_terminal(state):
    """
    return True if the game is over (When all of the piles have 2 coins or less)
    """
    
    # If any pile has more than 2 coins, game is still on. If not, the game is over
    for i in state:
        if i > 2:
            return False

    return True

def utility_of(state):
    """
    returns 0 if winner is MAX player, 1 if winner is MIN player
    MIN starts the game
    """
    # We can check that if the length is odd the winnner is 1-MAX otherwise if length is even the winner is O-MIN
    if len(state) % 2 == 0:
        return 0

    return 1

def successors_of(state):
    """
    returns a list of tuples (move, state)
    move indicates which pile we split
    """
    
    sucList = []

    # Need to take the list and find the next divisions of the piles

    # Number of coins on current pile we are on at the time
    pileNum = 0

    # For each item of the state we want to split it into two piles and add that new state to our list of tuples
    # We know already that the state is not terminal so we dont need to check it again
    for i in range(0,len(state)):
        pileNum = state[i]
        if state[i] > 2:
            for j in range (1, pileNum // 2 + 1):
                # We add the two new piles to our list of tuples               
                new_state = state[:i] + [j, (pileNum) - j] + state[i + 1:]
                sucList.append(new_state)

    return sucList

def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = minmax_decision(state)
    return new_state


def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [15]
    
    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))


if __name__ == '__main__':
    main()
