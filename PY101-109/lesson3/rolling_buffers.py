def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# checking the above code without running it the main difference is the way
# that items are added to the buffer, in the first version we are using a
# method that mutates the original buffer object while in the second version
# a new local version of the buffer is being created by the reassignment of 
# buffer, so we will see that the global version, the object being passed in
# will not be updated with the second version of the function.

buffer1 = []
buffer2 = []
max_buffer_size = 5

for element in range(6):
    add_to_rolling_buffer1(buffer1, max_buffer_size, element)
    add_to_rolling_buffer2(buffer2, max_buffer_size, element)

print(f"{buffer1 =} {buffer2 = }")

# outputs buffer1 =[1, 2, 3, 4, 5] buffer2 = [], as expected the second 
# version does not update the buffer list passed in as a new local 
# variable is being updated instead.