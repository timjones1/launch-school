import os

def valid_number(num):
    # check input num is a non_negative number (can be zero)
    # that can be cast to float
    try:
        float(num)
    except ValueError:
        return False

    if num in ["nan", "inf"]:
        return False

    return float(num) >= 0

def valid_duration(num):
    # check input num is a positive number that can be cast to float
    try:
        float(num)
    except ValueError:
        return False
    
    return float(num) > 0

def prompt(str_input):
    # add a ==> to the str_input before printing
    print(f"==>{str_input}")


while True:
    # main programme
    loan_amount = input("Please enter the loan amount in pounds and pence "\
    "e.g. 1000.00 \n")

    while not valid_number(loan_amount):
        prompt("That is not a valid number, please try again:")
        loan_amount = input()

    apr_interest_rate = input("Please enter the loan APR interest rate,"\
        " for example for 5% enter 5,\nfor 7.5% enter 7.5: \n")

    while not valid_number(apr_interest_rate):
        prompt("This is not a valid interest rate, please enter a positive" \
               " number:")
        apr_interest_rate = input()

    monthly_interest_rate = float(apr_interest_rate) / 12 / 100

    loan_duration_months = input("Please enter the duration of the loan in " \
                                 "months, as a positive number: \n")

    while not valid_duration(loan_duration_months):
        prompt("This is not a valid loan duration, please enter a positive " \
               "number")
        loan_duration_months = input()

    loan_amount = float(loan_amount)
    loan_duration_months = float(loan_duration_months)

    # deal with possible zero interest rate value
    if monthly_interest_rate > 0:
        monthly_repayment = loan_amount * (monthly_interest_rate / \
            (1 -(1 + monthly_interest_rate) ** -loan_duration_months))
    else:
        monthly_repayment = loan_amount / float(loan_duration_months)

    # return the calculated monthly repayment
    prompt(f"The monthly repayment amount is: £{'%.2f' % monthly_repayment}")

    # ask if another calculation is required
    keep_calculating = input("would you like to do another calculation? " \
                             "press n to exit or any other key to continue: ")

    if keep_calculating.lower() == "n":
        break

    os.system('clear')