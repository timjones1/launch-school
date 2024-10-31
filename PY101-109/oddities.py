def oddities(in_list):
    
    out_list = []
    
    if len(in_list) == 0:
        return out_list

    for i in range(0, len(in_list), 2):
        out_list.append(in_list[i])
    
    return out_list

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

# so we can also use index slicing, to achieve the same result
# index slicing allows us to specify [start:stop:stride], as is usual
# start is inclusive but stop is exclusive, stride is usually left blank
# and defaults to 1. 

print([2,3,4,5,6][1::2]) #start is 1 (so second item), stride 2 = [3,5]

# to solve the oddities problem using slicing we can just leave start and
# stop parameters blank and specify stride of 2.

def sliced_oddities(a_list):
    return a_list[::2]

print("sliced oddities tests:")

print(sliced_oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(sliced_oddities([1, 2, 3, 4]) == [1, 3])        # True
print(sliced_oddities(["abc", "def"]) == ['abc'])     # True
print(sliced_oddities([123]) == [123])                # True
print(sliced_oddities([]) == [])                      # True
