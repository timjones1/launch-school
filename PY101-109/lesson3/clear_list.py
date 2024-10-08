'''
clear the numbers from a list'''

#two different methods

numbers = [1, 2, 3, 4]


#first solution , nice and simple , just use the clear method

# numbers.clear()

# my seocnd soluition is 

for number in range(len(numbers)):
    numbers.pop()

print(numbers)

# there is a much simpler way to do this, as we are clearing the array with 
# pop() it will eventually be empty, we can use this Falsey state as the 
# condition to terminate a while loop, which will make for clearer control
# logic as below.

print("solution 2, using pop()")

numbers = [1, 2, 3, 4, 5]

print(f"{numbers = }")

while numbers:
    numbers.pop()
    

print(numbers)