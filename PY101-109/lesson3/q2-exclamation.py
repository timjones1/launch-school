str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def ends_in_exclamation(in_string):

    if len(in_string) == 0:
        return False
    elif in_string[-1] == "!":
        return True
    else:
        return False

print(ends_in_exclamation(str1)) # True
print(ends_in_exclamation(str2)) # False
print(ends_in_exclamation("")) # False

# on reveiwing the solution it would have been easier to use the String method endswith()

print(str1.endswith("!")) # True
print(str2.endswith("!")) # False
