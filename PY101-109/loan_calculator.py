def valid_positive_number(num):
    # check input num is a positive number that can be cast to float    
    try:
        float(num) 
    except ValueError:
        return False
    return float(num) >= 0

def prompt(str_input):
    # add a ==> to the str_input before printing
    print(f"==>{str_input}")


def main():
    # main programme 
    loan_amount = input("Please enter the loan amount in pounds and pence "\
    "e.g. 1000.00 \n")

    while not(valid_positive_number(loan_amount)):
        prompt("That is not a valid positive number, please try again:")
        loan_amount = input()

    apr_interest_rate = input("Please enter the loan APR interest rate as a "\
        "positive number \nfor example for 5% enter 5, for 7.5% enter 7.5: \n")

    while not(valid_positive_number(apr_interest_rate)):
        prompt("This is not a valid interest rate, please enter a positive" \
               " number:")
        apr_interest_rate = input()

    monthly_interest_rate = float(apr_interest_rate) / 12 / 100

    loan_duration_months = input("Please enter the duration of the loan in " \
                                 "months, as a positive number \n")

    while not valid_positive_number(loan_duration_months):
        prompt("This is not a valid loan duration, please enter a positive " \
               "number \n")
        loan_duration_months = input()

    monthly_repayment = float(loan_amount) * (monthly_interest_rate / (1 -(1 + monthly_interest_rate) **- float(loan_duration_months)))

    prompt(f"The monthly repayment amount is: £{'%.2f' % monthly_repayment}")

main()