'''
answering Q2 of PY101 Lesson 3 
'''

STR1 = "Come over here!"  # True
STR2 = "What's up, Doc?"  # False

def ends_in_exclamation(in_string):

    if len(in_string) == 0:
        return False
    return in_string[-1] == "!"

print(ends_in_exclamation(STR1)) # True
print(ends_in_exclamation(STR2)) # False
print(ends_in_exclamation("")) # False

# on reveiwing the solution it would have been easier to use the String method endswith()

print(STR1.endswith("!")) # True
print(STR2.endswith("!")) # False
