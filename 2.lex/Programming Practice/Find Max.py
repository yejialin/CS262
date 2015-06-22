# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

# Example:

l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f = len

# Try it on your own!
def findmax(f, l):
    tmp = None
    for n in range(len(l)):
        if (tmp == None or 
            f(l[n]) > tmp):
            tmp = f(l[n])
    return tmp

print findmax(f, l)

