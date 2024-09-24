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
    return float(num) >= 0

def prompt(str_input):
    print(f"==>{str_input}")

loan_amount = input("please enter the loan amount in pounds and pence\
e.g. 1000.00 \n")

while not(validate_number(loan_amount)):
    prompt("That is not a valid number, please enter a number e.g 500.00")
    loan_amount = input()

apr_interest_rate = input("please enter the loan interest rate as a positive number, \
for example for 5% enter 5, for 7.5% enter 7.5 \n")

while not(validate_positive_number(apr_interest_rate)):
    prompt("This is not a valid interest rate, please enter a positive number")
    apr_interest_rate = input()

monthly_interest_rate = float(apr_interest_rate) / 12

loan_duration_months = input("please enter the duration of the loan in months, as a positive number \n")

while not(validate_positive_number(loan_duration_months)):
    prompt("This is not a valid loan duration, please enter a positive number")
    loan_duration_months = input()

monthly_repayment = float(loan_amount) * (monthly_interest_rate / (1 -(1 + monthly_interest_rate) **- float(loan_duration_months)))

prompt(f"The monthly repayment amount is: £{"%.2f" % monthly_repayment}")