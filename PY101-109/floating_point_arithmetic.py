
float1 = float(input("==> Enter the first number:") or 3.141529)
float2 = float(input("==> Enter the second number:") or 2.718282)

'''
print(f"{float1} + {float2} = {float1 + float2}")
print(f"{float1} - {float2} = {float1 - float2}")
print(f"{float1} * {float2} = {float1 * float2}")
print(f"{float1} / {float2} = {float1 / float2}")
print(f"{float1} // {float2} = {float1 // float2}")
print(f"{float1} % {float2} = {float1 % float2}")
print(f"{float1} ** {float2} = {float1 ** float2}")

# above is the repetetive way of doing things.

there are a few different ways to solve this
one uses eval() to evalute a function.
to use eval, we could store the operators in a list
then loop through them and evaluate and print the statements.
'''

ops = ["+","-","*","/","//","%","**"]


''' concise solution
for op in ops:
    eval_string = f"{float1} {op} {float2}"
    print(f"{eval_string} = {eval(eval_string)}")

'''

# another solution is to use a case statement inside a function to
# calculate the answer

def calculate(num1,num2, opn):

    match opn:
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '*': return num1 * num2
        case '/': return num1 / num2
        case '//': return num1 // num2  
        case '%': return num1 % num2
        case '**': return num1 ** num2

for op in ops:
    result = calculate(float1, float2, op)
    print(f'{float1} {op} {float2} = {result}')

