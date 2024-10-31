# very simple xor solution

def xor(first, second):

    return first != second

print(xor(0,1))
print(xor(1,0))
print(xor(1,1))
print(xor(0,0))

def xor_1(first, second):

    return ((first and not second) or (not first and second))

print(xor_1(0,1))
print(xor_1(1,0))
print(xor_1(1,1))
print(xor_1(0,0))

# we have to add the bool function in front as otherwise python 
# short circuiting will return a 0 or 1 value if only the first half o
# of the condition is executed.