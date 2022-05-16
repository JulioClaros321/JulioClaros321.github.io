import datetime
from datetime import datetime

#entries = [("2015-01-01", "joe@signifyd.com", "PURCHASE"),
    #("2015-02-01", "fraudster@fraud.com", "FRAUD_REPORT"),
    #("2015-02-03", "fraudster@fraud.com", "FRAUD_REPORT"),
    #("2015-02-10", "joe@signifyd.com", "PURCHASE"),
    #("2015-02-14", "fraudster@fraud.com", "PURCHASE"),
    #("2015-03-15", "joe@signifyd.com", "PURCHASE"),
    #("2015-05-01", "joe@signifyd.com", "PURCHASE"),
    #("2015-10-01", "joe@signifyd.com", "PURCHASE"),
       #]


def event_processor(entries):
    '''Function takes a series of event objects, formats the date and uses list
    comprehension to organize customer outputs on the purchase trigger event'''

    database = []
    for event in entries:
        date = datetime.strptime(event[0], "%Y-%m-%d").date()
        email = event[1]
        action = event[2]

        database.append((date, email, action))

        if action != "PURCHASE":
            continue
        else:
            updated_data = [item for item in database if item[1] == email]
            fraud = [item for item in updated_data if item[2] == "FRAUD_REPORT"]
            good_hist = [item for item in updated_data if
                         (date - item[0]).days > 90]

            uncomf_hist = [item for item in updated_data if
                           (date - item[0]).days < 90]

            if len(updated_data) == 1:
                print(",".join((event[0], email, "NO_HISTORY")))

            elif len(fraud) > 0:
                print(",".join((event[0], email, "FRAUD_HISTORY:"
                                + str(len(fraud)))))

            elif len(good_hist) >= 1:
                print(",".join((event[0], email, "GOOD_HISTORY:"
                               + str(len(good_hist)))))

            else:
                print(",".join((event[0], email, "UNCONFIRMED_HISTORY:" +
                      str(len(uncomf_hist) - 1))))






if __name__ == '__main__':
    event_processor(entries)