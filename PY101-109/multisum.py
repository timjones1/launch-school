
def multisum(upto_num, multiples=[3,5]):
    
    sum_total = 0
    
    for numerator in range(upto_num+1):
        for divisor in multiples:
            if numerator % divisor == 0:
                sum_total += numerator
                break
    
    return sum_total

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
