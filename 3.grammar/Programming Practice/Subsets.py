# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def sublist(total, choose):
    if total == []:
        return [choose]
    else:
        current = total[0]
        rest = total[1:]    
        return sublist(rest, choose + [current]) + sublist(rest, choose)              
    
list = ['Sam', 'Jack', 'Karl']
choose = []
print sublist(list, choose)
