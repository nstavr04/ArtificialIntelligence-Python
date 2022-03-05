class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for node in list:
        queue.append(node)
    return queue


'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    return queue.pop(0)


'''
Successor function, mapping the nodes to its successors
We do not include the ones that violate our problems constraints
'''
def successor_fn(state):  # Lookup list of successor states

    violation = [('W','E','E','W'), ('E','W','W','E'),('W','W','E','E'),('E','E','W','W')]

    return [i for i in STATE_SPACE[state] if i not in violation]  

# (Farmer, Wolf, Goat, Cabbage)
# Wolf and Goat cannot be together alone W E E W || E W W E
# Goat and Cabbage cannot be together alone W W E E || E E W W

ST1 = ('W','W','W','W')
ST15 = ('E','W','W','W') # Case where farmer just goes alone

ST2 = ('E','E','W','W') # VIOLATION
ST3 = ('E','W','E','W')
ST4 = ('E','W','W','E') # VIOLATION

ST5 = ('W','E','W','W')
ST6 = ('W','W','E','W')
ST7 = ('W','W','W','E')

ST8 = ('E','E','E','W')
ST9 = ('E','E','W','E')
ST10 = ('E','W','E','E')

ST11 = ('W','E','E','W') # VIOLATION
ST12 = ('W','E','W','E') # SOLUTION PATH
ST13 = ('W','W','E','E') # VIOLATION

ST14 = ('E','E','E','E')

INITIAL_STATE = ST1
GOAL_STATE = ST14
STATE_SPACE = { ST1: [ST2, ST3, ST4, ST15],
                ST15: [ST1],
               ST2: [ST1, ST5], ST3: [ST1, ST6], ST4: [ST1, ST7],
               ST5: [ST2, ST8, ST9], ST6: [ST3, ST9, ST10], ST7: [ST4, ST9, ST10],
               ST8: [ST5, ST6, ST11], ST9: [ST5, ST7, ST12], ST10: [ST6, ST7, ST13],
               ST11: [ST8, ST14], ST12: [ST9, ST14], ST13: [ST10, ST14],
               ST14: [] }


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
