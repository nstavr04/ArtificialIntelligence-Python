A = 'A' 
B = 'B' 
percepts = [] 
table = {
    ((A, 'Clean'),): 'Right', 
    ((A, 'Dirty'),): 'Suck', 
    ((B, 'Clean'),): 'Left', 
    ((B, 'Dirty'),): 'Suck', 
    ((A, 'Clean'), (A, 'Clean')): 'Right', 
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',
    #...
    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right', 
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck', 
    ((A, 'clean'), (A, 'Dirty'), (B, 'clean')): 'Left',
    #...
}

def LOOKUP(percepts, table): # Lookup appropriate action for percepts
    action = table.get(tuple (percepts)) 
    return action

def TABLE_DRIVEN_AGENT (percept): # Determine action based on table and percepts
    percepts.append(percept) # Add percept 
    action = LOOKUP(percepts, table) # Lookup appropriate action for percepts 
    return action

def run(): # run agent on several sequential percepts
    print('Action\tPercepts') 
    print(TABLE_DRIVEN_AGENT ((A, 'Clean')), '\t', percepts) 
    print (TABLE_DRIVEN_AGENT ((A, 'Dirty')), '\t', percepts) 
    print(TABLE_DRIVEN_AGENT ((B, 'Clean')), '\t', percepts)

def main():
    run()

if __name__ == '__main__':
    main()

#   3.How many table entries would be required if only the current percept was used to select and
#   action rather than the percept history?
#
#   Just one
#
#   4.How many table entries are required for an agent lifetime of T steps?
#
#   T table entries

