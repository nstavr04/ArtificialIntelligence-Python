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
Run the A* algorithm
'''
def A_STAR():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_LOWEST_FN(fringe)
        if H[node.STATE] == GOAL_H:
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
Insert the next node with the best fn
'''
def INSERT_ALL(list, queue):
    queue.extend(list)
    return queue


'''
Removes and returns the child with the lowest fn function value
'''
# Need to calculate path cost
def REMOVE_LOWEST_FN(queue):
    min = queue[0]
    if(min.STATE[0] == 'A'):
        min_fn = 0
    else:
        min_fn = fn(min)
        for node in queue:
            if fn(node) < min_fn:
                min = node
                min_fn = fn(node)
    
    queue.remove(min)
    return min

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']

def hn(x):
    return H[x.STATE]

def gn(x):
    return COST[(x.PARENT_NODE.STATE, x.STATE)]

def fn(x):
    return hn(x) + gn(x) 

# Our state space

ST1 = ('A', 'Dirty', 'Dirty')
ST2 = ('B', 'Dirty', 'Dirty')
ST3 = ('A', 'Clean', 'Dirty')
ST4 = ('B', 'Clean', 'Dirty')
ST5 = ('A', 'Dirty', 'Clean')
ST6 = ('B', 'Dirty', 'Clean')
ST7 = ('A', 'Clean', 'Clean')
ST8 = ('B', 'Clean', 'Clean')

INITIAL_H = 3
GOAL_H = 0
INITIAL_STATE = ST1
STATE_SPACE = { INITIAL_STATE: [ ST2, ST3],
               ST2: [ST1, ST6], 
               ST3: [ST4],
               ST4: [ST3,ST8], 
               ST5: [ST6, ST7], 
               ST6: [ST5],
               ST7: [],
               ST8: [] }

COST = {
    (ST1, ST2): 1, (ST1, ST3): 1, 
    (ST2, ST1): 1, (ST2, ST6): 1,
    (ST3, ST4): 1, 
    (ST4, ST3): 1, (ST4, ST8): 1,
    (ST5, ST6): 1, (ST5, ST7): 1, 
    (ST6, ST5): 1
}

H = {
    ST1: 3, ST2: 3, ST3: 2, ST4: 1, ST5: 1, ST6: 2, ST7: 0, ST8: 0 
}


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = A_STAR()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
