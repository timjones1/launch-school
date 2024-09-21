''' Calculator exercise with bonus additions
'''

language = "fr" #choose from en, fr

configs = {}

with open(f'{language}_config.ini',"r") as file:

    lines = file.readlines()

    for line in lines:
        key, value = line.strip().split("=")
        configs[key] = value

def prompt(message):
    ''' add ==> to prints to the console'''
    print(f"==>{message}")

def invalid_number(number_str):
    ''' check if numeric input is a valid integer'''
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt(configs['welcome'])

keep_calculating = True

while keep_calculating:

    prompt(configs['first'])
    number1 = input()

    while invalid_number(number1):
        prompt(configs['invalid'])
        number1 = input()

    prompt(configs['second'])
    number2 = input()

    while invalid_number(number2):
        prompt(configs['invalid'])
        number2 = input()

    prompt(configs['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt("please enter 1, 2, 3 or 4")
        operation = input()

    match operation:

        case '1':   # '1' represents addition
            output = float(number1) + float(number2)
        case '2': # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3': # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4': # '4' represents division
            output = float(number1) / float(number2)

    print(f"{configs['result']}{output}")

    prompt(configs['continue?'])

    keep_calculating = input() == "y"