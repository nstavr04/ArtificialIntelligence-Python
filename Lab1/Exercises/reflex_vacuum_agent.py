A = 'A'
B = 'B'

Environment = {
    A: 'Dirty', 
    B: 'Dirty', 
    'Current': A
}

# Determine action
def REFLEX_VACUUM_AGENT(loc_st): 
    if loc_st[1] == 'Dirty':
        return 'Suck' 
    if loc_st[0] == A:
        return 'Right' 
    if loc_st[0] == B:
        return 'Left'

def Sensors(): # Sense Environment
    location = Environment['Current'] 
    return (location, Environment[location])

def Actuators (action): # Modify Environment
    location = Environment['Current'] 
    if action == 'Suck':
        Environment[location] = 'Clean' 
    elif action == 'Right' and location == A:
        Environment['Current'] = B 
    elif action == 'Left' and location == B:
        Environment['Current'] = A

def run(n): # run the agent through n steps 
    print('     Current                      New') 
    print('location status action location status') 
    for i in range(1, n):
        (location, status) = Sensors() # Sense Environment before action 
        print("{:12s}{:8s}".format(location, status), end='') 
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors() # Sense Environment after action 
        print("{:8s}{:12s}{:8s}".format(action, location, status))

run(10)

#   Should bogus actions be able to corrupt the environment? Change the
#   REFLEX_VACUUM_AGENT to return bogus action, such as Left when it should go Right etc.
#   Run the agent. Do the Actuators allow bogus actions?
#
#   Because we only have 2 locations, either way it goes to the other one
#   So the environment gets corrupted but it still works as intended