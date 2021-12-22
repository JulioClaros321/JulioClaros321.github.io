import math


def get_min_payment(P, r, mort=30, n=12):
    A = (P * r(1 + r) ** n) / (((1 + r) ** n) - 1)



def REAL_get_min_payment(principal, interest_rate, mortgage_term=30,
                         num_annual_payments=12):
    """ Calculate the minimum payment of a mortgage.

    Args:
        principal (number): the total amount borrowed.
        interest_rate (float): the annual interest rate of the mortgage
            (should be between 0 and 1).
        mortgage_term (int): the term of the mortgage in years (default
            is 30).
        num_annual_payments (int): the number of payments due per year
            (default is 12).

    Returns:
        (int): the minimum mortgage payment.
    """
    P = principal
    r = interest_rate / num_annual_payments
    n = num_annual_payments * mortgage_term
    return ceil((P * r * (1 + r) ** n) / ((1 + r) ** n - 1))


"""
Function computes the amount of interst due in the next payment 

Args:
    b (int) = balance of the mortgage 
    r (int) = annual interest rate 
    n (int) = the number of payments per year, default = 12

Returns:
    the amount of interest due in the next payment 
"""


def interest_due(b, r, n=12):
    i = b * r
    return i


def interest_due(balance, interest_rate, num_annual_payments=12):
    """ Calculate the interest due on a given payment.

    Args:
        balance (number): the unpaid portion of the loan principal.
        interest_rate (float): the annual interest rate of the mortgage
            (should be between 0 and 1).
        num_annual_payments (int): the number of payments due per year
            (default is 12).

    Returns:
        (float): the interest due on the next payment.
    """
    b = balance
    r = interest_rate / num_annual_payments
    return b * r


"""
Funtion 

Args:
    b (int) = balance of the mortgage
    r (int) = annual interest rate 
    p (int) = amount user wants to pay per payment 
    n (int) = the number of payments per year, default = 12    
"""