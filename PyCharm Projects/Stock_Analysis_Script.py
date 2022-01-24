import robin_stocks.robinhood as rs
import pyotp
import pandas as pd
import datetime
from pprint import pprint
import getpass


class Investor:
    def __init__(self, email, password, volatility, lock_in_profit_time):
        self.email = email
        self.password = password
        self.volatility = volatility
        self.lock_in_profit_time = lock_in_profit_time
        self.active = True


def sense():
    return true

def get_portfolio():
    mystocks = rs.build_holdings()
    for key, value in mystocks.items():
        print(key, value)


def calculate_annual_return(ending_prices):
    return round((100 * ((ending_prices[len(ending_prices) - 1] - ending_prices
    [0]) / (ending_prices[0]))), 2)


def get_average_volume(stock_name):
    temp = rs.stocks.get_stock_historicals(stock_name,
                                           interval="day",
                                           span="year",
                                           bounds="regular",
                                           info="volume")

    average_volume = sum(temp) / (len(temp) - 1)

    return average_volume


def login(robinhood_email, password):

    return True


def create_stock_history_dataframe(stock_list, time_frame):
    symbol_data = rs.stocks.get_stock_historicals(stock_list,
                                                  interval="day",
                                                  span=time_frame,
                                                  bounds="regular")

    uncleaned_dataframe = pd.DataFrame(data=symbol_data)

    symbol = []
    date = []
    opening_price = []
    closing_price = []
    volume = []

    column_names = ["Symbol", "Date", "Opening Price", "Closing Price",
                    "Volume"]
    ticker_dataframe = pd.DataFrame(columns=column_names)

    for index, row in uncleaned_dataframe.iterrows():
        uncleaned_date = row["begins_at"][:10]
        year = uncleaned_date[:4]
        month = uncleaned_date[5:7]
        day = uncleaned_date[8:10]
        reformated_date = datetime.datetime(int(year), int(month), int(day), 0,
                                            0, 0)
        clean_date = reformated_date.strftime("%a %b %d %Y")

        symbol.append(row["symbol"])
        date.append(clean_date)
        closing_price.append(round(float(row["close_price"]), 2))
        volume.append(row["volume"])
        opening_price.append(round(float(row["open_price"]), 2))

    ticker_dataframe["Symbol"] = symbol
    ticker_dataframe["Date"] = date
    ticker_dataframe["Opening Price"] = opening_price
    ticker_dataframe["Closing Price"] = closing_price
    ticker_dataframe["Volume"] = volume

    return ticker_dataframe


def stock_recommendations_long_term_year(sector_symbols_list, sector_name, vol):
    year = "year"
    stock_recommendations = {}
    average_list = []
    removed_counter = 0
    kept_counter = 0
    rate_counter = 0
    rate_of_return_list = []

    for stocks in sector_symbols_list:
        average_volume = get_average_volume(stocks)

        if average_volume > vol:
            stock_name = rs.get_name_by_symbol(stocks)

            stock_data = create_stock_history_dataframe(stocks, year)

            ending_prices = stock_data["Closing Price"]

            average_trading = sum(ending_prices) / (len(ending_prices) - 1)

            rate_of_return = calculate_annual_return(ending_prices)
            if rate_of_return < 10:
                removed_counter = removed_counter + 1
            else:
                stock_recommendations[stock_name] = stock_data
                average_list.append(average_trading)
                rate_of_return_list.append(rate_of_return)
                kept_counter += 1
        else:
            removed_counter = removed_counter + 1
            continue

    print(len(sector_symbols_list), "Total Stocks Filtered Through Sector:",
          sector_name)
    print(removed_counter, "Stocks Removed")
    print(kept_counter, "Stocks That Met Criteria")
    print()

    for key in stock_recommendations:
        print("Stock Name: " + key)
        print("---------------------------------------------------------------")
        print(stock_recommendations[key])

        print("Annual Rate of Return This Year:",
              rate_of_return_list[rate_counter], "Percent")

        print("250 Day Moving Average:",
              round(average_list[rate_counter], 2), "(Solid Entry Point)")

        get_stock_earnings(stock_recommendations[key]["Symbol"][0])
        print()

        rate_counter += 1
        print()


def stock_recommendations_month_swing(sector_symbols_list, sector_name, vol):
    """ Function takes a list of ticker symbols, and returns a dataframe of
    stocks, trading a certain percentage lower than yearly averages (swings)"""

    year = "year"
    stock_recommendations = {}
    removed_counter = 0
    kept_counter = 0
    counter = 0
    percentages_list = []
    current_price_list = []
    average_list = []

    for stocks in sector_symbols_list:
        average_volume = get_average_volume(stocks)

        if average_volume > vol:
            stock_name = rs.get_name_by_symbol(stocks)
            stock_data = create_stock_history_dataframe(stocks, year)

            ending_prices = stock_data["Closing Price"]
            month_ending_prices = ending_prices[-20:]

            year_closing_average = round(
                (sum(ending_prices)) / (len(ending_prices)), 2)

            month_closing_average = round(
                (sum(month_ending_prices) / len(month_ending_prices)), 2)

            current_price = float(rs.stocks.get_latest_price(stocks)[0])

            percent_change_mtoy = 100 * ((month_closing_average -
                                          year_closing_average) / year_closing_average)

            percent_change_dtom = 100 * ((current_price - month_closing_average)
                                         / month_closing_average)

            if percent_change_dtom < -5 or percent_change_mtoy < -5:

                stock_recommendations[stock_name] = stock_data

                tuple = (float(percent_change_dtom), float(percent_change_mtoy))
                percentages_list.append((tuple))
                average_list.append(year_closing_average)
                current_price_list.append(current_price)

                kept_counter += 1
            else:
                removed_counter += 1

        else:
            removed_counter += 1
            continue

    print(len(sector_symbols_list),
          "Total Stocks Filtered Through Sector:", sector_name)

    print(removed_counter, "Stocks Removed")
    print(kept_counter, "Stocks That Met Criteria")
    print()

    for key in stock_recommendations:
        print("Stock Name: " + key)
        print("---------------------------------------------------------------")
        print(stock_recommendations[key])

        print("Current Price:", float(current_price_list[counter]), "(USD)")
        print("250 Day Moving Average:",
              round(average_list[counter], 2), "(Solid Entry Point)")

        print("Trading", round(percentages_list[counter][1], 2),
              "Percent This Month Compared To The Year And Trading",
              round(percentages_list[counter][0], 2),
              "Percent Right Now Compared "
              "To The Current Month")

        print()
        get_stock_earnings(stock_recommendations[key]["Symbol"][0])
        print()

        counter += 1
        print()


def stock_recommendations_week_swing(sector_symbols_list, sector_name, vol):
    week = "week"
    percent_change_list = []
    stock_recommendations = {}
    remove_counter = 0
    kept_counter = 0
    print_counter = 0

    for stocks in sector_symbols_list:
        average_volume = get_average_volume(stocks)

        if average_volume > vol:
            stock_name = rs.get_name_by_symbol(stocks)
            stock_data = create_stock_history_dataframe(stocks, week)

            ending_prices = stock_data["Closing Price"]
            if len(ending_prices) == 0:
                continue
            else:
                average_closing_price = round(
                    (sum(ending_prices)) / (len(ending_prices)), 2)

                current_price = float(rs.stocks.get_latest_price(stocks)[0])

                percent_day_change = 100 * ((current_price - ending_prices
                [len(ending_prices) - 1]) / (ending_prices[
                    len(ending_prices) - 1]))

                percent_change = 100 * (
                            (current_price - average_closing_price) /
                            (average_closing_price))

                if (percent_change > -10 or percent_day_change < -7):
                    remove_counter += 1
                else:
                    my_tuple = (percent_change, percent_day_change)
                    percent_change_list.append(my_tuple)
                    stock_recommendations[stock_name] = stock_data
                    kept_counter += 1
        else:
            remove_counter += 1
            continue

    print()
    print(len(sector_symbols_list),
          "Total Stocks Filtered Through In This Sector:", sector_name)

    print(remove_counter, "Stocks Removed")

    print(kept_counter, "Stocks That Met Criteria")

    for key in stock_recommendations:
        print("Stock Name: " + key)
        print("---------------------------------------------------------------")
        print(stock_recommendations[key])
        print()

        print("Down", round(percent_change_list[print_counter][0], 2),
              "Percent On The Week And Down",
              round(percent_change_list[print_counter][1], 2),
              "Percent On The Day")

        print_counter += 1
        print()


def get_stock_earnings(symbol):
    earnings = rs.get_earnings(symbol, info="eps")
    list_of_earnings = []

    for items in earnings:
        for keys in items:
            if keys == "actual":
                if items[keys] == None:
                    continue
                else:
                    list_of_earnings.append(float(items[keys]))

    if not list_of_earnings or (len(list_of_earnings) <= 2):
        print("Stock Doesnt Have Earnings or Not Enough Earnings Data")
    else:
        last_earnings = list_of_earnings[0]
        second_current = list_of_earnings[len(list_of_earnings) - 2]
        most_current = list_of_earnings[len(list_of_earnings) - 1]

        if last_earnings < second_current < most_current > 0:
            print("Q Earnings Reported (Price Per Share):", list_of_earnings)
            print("Company Is Demonstrating Profit And Beating Previous "
                  "Earnings")

        elif last_earnings < second_current < most_current < 0 or \
                (last_earnings > second_current < most_current < 0):
            print("Q Earnings Reported (Price Per Share):", list_of_earnings)
            print("Company May Not Be Currently Not Profitable But May be "
                  "Nearing Profitability")

        elif last_earnings > second_current < most_current < 0:
            print("Q Earnings Reported (Price Per Share):", list_of_earnings)
            print("Potential Bad Quarter, But Nearing Profitability And "
                  "Demonstrating Growth")

        elif (last_earnings > second_current < most_current > 0) or \
                (last_earnings < second_current > most_current > 0):
            print("Q Earnings Reported (Price Per Share):", list_of_earnings)
            print("Potential Bad Quarter(s), But Demonstrating Profitability")

        else:
            print("Q Earnings Reported (Price Per Share):", list_of_earnings)
            print("Company Earnings Inconsistent Or Losing Money, Higher "
                  "Risk/Reward Potential If It Were To Become Profitable ")


def main_loop(robinhood_email, password):
    current_user = Investor(robinhood_email, password, None, None)

    while current_user.active:

        current_user.volatility = \
            int(input("Set Volume (20M+) Usually Safer And Less Volatile: "))

        current_user.lock_in_profit_time = \
            input("Type of Investing: Year(Long), Month(Swing), Week(Swing): ")

        print("SECTORS: ")
        pprint("Aerospace, Agriculture, Apparel, Automotive, Banking, "
               "Construction, China, Defense, Energy, Engineering, "
               "Entertainment, ETF(Safer), Finance, Medical, Healthcare, "
               "Information-Technology, Large-Cap(ETF), Media, Oil, "
               "Pharmaceutical, Real-Estate, Retail, Small-Cap(ETF), "
               "Technology, Telecommunications, Transportation, Travel, "
               "US, Utilities")

        print()

        sectors = input("Enter Market Sector Interest (Sep. By Comma): ")

        if "," not in sectors:
            sector_list = [sectors]
        else:
            sector_list = (sectors.replace(" ", "")).split(",")

        for sector_name in sector_list:
            sector_symbol_list = rs.get_all_stocks_from_market_tag(
                tag=sector_name.lower(), info="symbol")

            if current_user.lock_in_profit_time.lower() == "year":
                stock_recommendations_long_term_year(sector_symbol_list,
                                                     sector_name.upper(),
                                                     current_user.volatility)

            elif current_user.lock_in_profit_time.lower() == "month":
                stock_recommendations_month_swing(sector_symbol_list,
                                                  sector_name.upper(),
                                                  current_user.volatility)

            else:
                stock_recommendations_week_swing(sector_symbol_list,
                                                 sector_name.upper(),
                                                 current_user.volatility)

            print(
                "-------------------------------------------------------"
                "----------")
            print()

        repeat = input("Refine Your Searches? (Y/N): ")
        if repeat.upper() == "N": current_user.active = False

    rs.logout()


def main():
    robinhood_email = input("Enter Email For Robinhood: ")
    password = getpass.getpass("Enter Password: ")

    if not login(robinhood_email, password):
        return 0

    else:
        main_loop(robinhood_email, password)


if __name__ == '__main__':
    main()