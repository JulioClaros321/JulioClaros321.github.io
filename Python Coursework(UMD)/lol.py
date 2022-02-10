def is_leap_year(number):
    year = int(number)
    if year < 1582:

        print("none")
    elif year >= 1582:
        if year % 100 != 0 and year % 4 == 0:

            print("true")
        elif year % 100 == 0 and year % 400 == 0:

            print("true")
        elif year % 400 == 0:

            print("true")
        else:
            print("false")

is_leap_year(2200)