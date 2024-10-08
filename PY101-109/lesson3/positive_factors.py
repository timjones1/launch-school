def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# print(factors(-10))

# this sets off an infinite loop as we are decrementing an
# already negative number and it is always gonig to be lower than zero.

# we should be able to fix this by changing line 4, to divisor > 0 so 
# that it exists immediately for negative numbers, as we are not looking
# for factors of negative numbers

def positive_factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(positive_factors(10))
print(positive_factors(-2))