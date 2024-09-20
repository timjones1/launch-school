def prompt(message):
    ''' add ==> to prints to the console'''
    print(f"==>{message}")

def invalid_number(number_str):
    ''' check if numeric input is a valid integer'''
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')

keep_calculating = True

while keep_calculating:

    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("this isnt a valid number:")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("this isnt a valid number:")
        number2 = input()

    prompt('''What operation would you like to perform?\n
        1) Add 2) Subtract 3) Multiply 4) Divide''')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt("please enter 1, 2, 3 or 4")
        operation = input()

    match operation:

        case '1':   # '1' represents addition
            output = int(number1) + int(number2)
        case '2': # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3': # '3' represents multiplication
            output = int(number1) * int(number2)
        case '4': # '4' represents division
            output = int(number1) / int(number2)

    print(f"The result is: {output}")

    prompt('press y if you would like to complete another calculation, or any other key to finish:')

    keep_calculating = (input() == "y")