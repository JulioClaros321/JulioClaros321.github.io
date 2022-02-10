""" Calculate minimum mortgage payment and number of payments required
to pay off a mortgage. """


from argparse import ArgumentParser
from math import ceil
import sys


def get_min_payment(principal, interest_rate, mortgage_term=30,
                num_annual_payments=12):

    P = principal
    r = interest_rate / num_annual_payments
    n = num_annual_payments * mortgage_term
    return ceil((P * r * (1 + r)**n) / ((1 + r)**n - 1))


def interest_due(balance, interest_rate, num_annual_payments=12):
    b = balance
    r = interest_rate / num_annual_payments
    return b * r


def remaining_payments(balance, interest_rate, payment_amount,
                       num_annual_payments=12):
    payments = 0
    while balance > 0:
        i = interest_due(balance, interest_rate, num_annual_payments)
        balance -= payment_amount - i
        payments += 1
    return payments


def main(principal, interest_rate, mortgage_term=30, num_annual_payments=12,
         target_payment=None):
    """ Calculate the minimum payment of a mortgage and the number of
    payments required to pay off the mortgage.
    
    Args:
        principal (number): the total amount of the mortgage.
        interest_rate (float): the annual interest rate, as a value
            between 0 and 1.
        mortgage_term (int, optional): the term of the mortgage in
            years. Defaults to 30.
        num_annual_payments (int, optional): the number of payments per
            year. Defaults to 12.
        target_payment (float, optional): the user's desired payment. If
            None, the minimum payment will be used. Defaults to None.
    
    Side effects:
        Writes to stdout.
    """
    min_payment = get_min_payment(principal, interest_rate, mortgage_term,
                                  num_annual_payments)
    print(f"Your minimum payment is ${min_payment}.")
    if target_payment is None:
        target_payment = min_payment
    if target_payment < min_payment:
        print(f"Your target payment is less than the minimum payment.")
    else:
        payments = remaining_payments(principal, interest_rate, target_payment,
                                      num_annual_payments)
        print(f"If you make payments of ${target_payment}, you will pay off"
              f" the mortgage in {payments} payments.")


def parse_args(arglist):
    """ Parse command line arguments.
    
    Args:
        arglist (list of str): a list of command line arguments.
            Required arguments:
                the total amount of the mortgage
                the annual interest rate (as a float between 0 and 1)
            Optional arguments:
                -t/--term: the term of the mortgage in years (defaults
                    to 30)
                -a/--num_annual_payments: the number of payments per
                    year (defaults to 12)
                -p/--target_payment: the target payment amount (defaults
                    to the minimum payment)
    
    Returns:
        (namespace) a namespace object as returned by
        argparse.ArgumentParser.parse_args().
    """
    parser = ArgumentParser()
    parser.add_argument("principal", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("interest_rate", type=float,
                        help="the annual interest rate (as a float between 0"
                             " and 1)")
    parser.add_argument("-t", "--term", type=int, default=30,
                        help="the term of the mortgage in years (defaults to"
                             "30)")
    parser.add_argument("-a", "--num_annual_payments", type=int,
                        default=12, help="the number of payments per year"
                                         " (defaults to 12)")
    parser.add_argument("-p", "--target_payment", type=float, default=None,
                        help="the target payment amount (defaults to the"
                             " minimum payment)")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.principal, args.interest_rate, args.term,
         args.num_annual_payments, args.target_payment)
