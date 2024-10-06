'''
reversing a list without mutating the original list.

we cannot use the string method reverse as this changes the order of the 
sequence in place which is mutating the original list

we can use slicing 
'''

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

numbers_reversed_sliced = numbers[::-1]

print(f"{numbers_reversed_sliced = }")

# why does this work, the slice notation includes [start : stop : step] as 
# three paramters for each dimension of the slice, so our range includes all
# items, as we havent specificed a specific start of stop character, and the 
# step is -1, this decreases the index by 1 each step starting from the end.

# We could used a copy of the original list and then use the reverse() method.

numbers_reversed = numbers.copy()

numbers_reversed.reverse()

print(f"{numbers_reversed = }")