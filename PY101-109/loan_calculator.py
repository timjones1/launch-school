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

    if num in ["nan", "inf"]:
        return False

    return float(num) > 0


def prompt(str_input):
    # add a ==> to the str_input before printing
    print(f"==>{str_input}")


def request_loan_amount():
    # request input of loan amount
    amount = input("Please enter the loan amount in pounds and pence "\
    "e.g. 1000.00 \n")

    while not valid_number(amount):
        prompt("That is not a valid number, please try again:")
        amount = input()

    return float(amount)


def request_interest_rate():
    # request input of interest rate to apply.
    apr_rate = input("Please enter the loan APR interest rate,"\
        " for example for 5% enter 5,\nfor 7.5% enter 7.5: \n")

    while not valid_number(apr_rate):
        prompt("This is not a valid interest rate, please enter a positive" \
               " number:")
        apr_rate = input()

    monthly_rate = float(apr_rate) / 12 / 100

    return monthly_rate


def request_loan_duration():
    # request input of loan duration with the option of years or months
    duration_months = input("Please enter the duration of the loan in " \

                                 "months, or press y to enter in years: \n")

    # validate alternative duration in years and convert to months
    if duration_months.lower() == "y":
        duration_years = input("Please enter the duration of the loan " \
                                 "in years: \n")
        while not valid_duration(duration_years):
            prompt("This is not a valid loan duration, please enter a " \
               "positive number")
            duration_years = input()

        duration_months = float(duration_years) * 12

    # validate duration if entered in months
    while not valid_duration(duration_months):
        prompt("This is not a valid loan duration, please enter a positive " \
               "number")
        duration_months = input()

    return float(duration_months)

def calculate_monthly_repayment(amount,interest_rate,
                                duration_months):
    # deal with possible zero interest rate value
    if interest_rate > 0:
        monthly_repayment = amount * (interest_rate / \
            (1 -(1 + interest_rate) ** - duration_months))
    else:
        monthly_repayment = amount / float(duration_months)

    # return the calculated monthly repayment
    prompt(f"The monthly repayment amount is: £{monthly_repayment:.2f}")


while True:
    os.system('clear')

    loan_amount = request_loan_amount()
    monthly_interest_rate = request_interest_rate()
    loan_duration_months = request_loan_duration()

    calculate_monthly_repayment(loan_amount,monthly_interest_rate,
                                loan_duration_months)

    # ask if another calculation is required
    keep_calculating = input("would you like to do another calculation? " \
                             "press n to exit or any other key to continue: ")

    if keep_calculating.lower() == "n":
        break