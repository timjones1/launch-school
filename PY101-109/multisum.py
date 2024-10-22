
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

# other methods

# official method splits the problem into smaller chunks

def is_divisible(numerator,divisor):

    return numerator % divisor == 0

def multisum_ls(max_number):

    multisum_total = 0

    for number in range(max_number+1):

        if is_divisible(number,5) or is_divisible(number,3):
            multisum_total += number
    
    return multisum_total

print(multisum_ls(3) == 3)
print(multisum_ls(5) == 8)
print(multisum_ls(10) == 33)
print(multisum_ls(1000) == 234168)

# one student solution wrapped everything into a list comp
# reimplement based on a conditional list comprehension

def multisum_usr(max_number):

    multiple_list = [x for x in range(max_number + 1) \
                     if x % 3 == 0 or x % 5 == 0]
    return sum(multiple_list)

print(multisum_usr(3) == 3)
print(multisum_usr(5) == 8)
print(multisum_usr(10) == 33)
print(multisum_usr(1000) == 234168)