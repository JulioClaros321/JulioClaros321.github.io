import robin_stocks.robinhood as rs
import pyotp
import pandas as pd
import datetime
from pprint import pprint
import getpass


def login():
    totp = pyotp.TOTP("ES5FN4MTEKBKBH2G").now()
    # print("Current OTP", totp)
    rs.login(username="Julio.claros321@gmail.com",
             password="IWe@rJeanShorts5",
             mfa_code=totp)

    return True

def main():
    login()
    sector_name = "New-york"

    sector_symbol_list = rs.get_all_stocks_from_market_tag(
                    tag=sector_name.lower(), info="symbol")

    print(sector_symbol_list)
    print(len(sector_symbol_list))


if __name__ == '__main__':
    main()