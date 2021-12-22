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


def remaining_payments (b, r, p, n = 12):
    interest_due = 0
    count = 0
    while true:
        if b > 0:
            b -= interest_due


def real_remaining_payments(balance, interest_rate, payment_amount,
                       num_annual_payments=12):
    """ Calculate the number of payments required to pay off the loan.

    Args:
        balance (number): the unpaid portion of the loan principal.
        interest_rate (float): the annual interest rate of the mortgage
            (should be between 0 and 1).
        payment_amount (number): the desired payment. Should be equal to
            or greater than the minimum payment as returned by
            get_min_payment().
        num_annual_payments (int): the number of payments due per year
            (default is 12).

    Returns:
        (int): the number of remaining payments.

    Raises:
        ValueError: payment_amount is less than the minimum payment.
    """
    payments = 0
    while balance > 0:
        i = interest_due(balance, interest_rate, num_annual_payments)
        balance -= payment_amount - i
        payments += 1
    return payments


if __name__ == '__main__':
    lol = real_remaining_payments(10000, 3, 20,)
    print(lol.payments)