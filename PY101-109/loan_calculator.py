def validate_number(num):
    
    try:
        float(num)
    except ValueError:
        return False
    return True

def validate_positive_number(num):
    
    try:
        float(num) 
    except ValueError:
        return False
    return num >= 0

def prompt(str_input):
    print(f"==>{str_input}")

loan_amount = input("please enter the loan amount in pounds and pence\
                    e.g. 1000.00")

while not(validate_number(loan_amount)):
    prompt("That is not a valid number, please enter a number e.g 500.00")

apr_interest_rate = input("please enter the loan interest rate as a positive number, \
                          for example for 5% enter 5, for 7.5% enter 7.5")

while not(validate_positive_number(apr_interest_rate)):
    prompt("This is not a valid interest rate, please enter a positive number")