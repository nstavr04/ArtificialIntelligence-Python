# Factorial done recursively and iteratively

def fact1(n):
    '''an example of documentation string'''
    ans = 1
    for i in range (2,n+1):
        ans = ans * i
    return ans

def fact2(n):
    if n < 1:
        return 1
    else:
        return n * fact2(n-1)

print(fact1(6))
print(fact2(200))

# This is how you can call the documentation string
help(fact1);