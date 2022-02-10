# Julio Claros
# 114153234
# 2018-11-9
# Assignment: HW 2


def get_user_info():
    """"
    This functions asks the user for input, using prompts, to establish how many credits a student is taking, their
    resident status, and eligibility for sen/jr surcharge. Then it calls function Calculate_tuition.
    """
    print("How many credits are you currently enrolled in?")
    credit = int(input())

    print("Are you a resident?")
    res_status = input()

    if res_status.lower() == "yes":
        res_status = True
    else:
        res_status = False

    print("Have you declared a major in: Business, Engineering, or Computer Science? Yes or No?")
    spec_major = input()

    if spec_major.lower() == "yes":
        print("Do you have junior or senior status? Yes or No?")
        diff_cost = input()

        if diff_cost.lower() == "yes":
            diff_cost = True
        else:
            diff_cost = False
    else:
        diff_cost = False

    calculate_tuition(credit, res_status, diff_cost)
# it takes and int, true/false, true/false


def calculate_tuition(credit, res_status, diff_cost):
    """"
    This function calculates a student's total tuition cost at UMD by matching up certain criteria entered by the users,
    which includes eligibility of certain fees.

    Args:
        credit (integer): Total number of credits a user is enrolling with
        res_status (Boolean expression): True if Resident, False if Non-Resident
        diff_cost (Boolean expression): True if eligible for sen/jr surcharge, False for not eligible.
    Return:
        total (float value): Total tuition value converted in floating point value
    """
    cred_hours = int(credit)

    if cred_hours == 0:
        tuition = 0
    elif (res_status is True) & (cred_hours >= 12):
        tuition = 6697.50
        if diff_cost is False:
            tuition = 5297.50

    elif (res_status is True) & (cred_hours < 12):
        if cred_hours < 9:
            mandatory = 453
            tuition = (cred_hours * 360) + mandatory
            if diff_cost is True:
                surcharge = (cred_hours * 116)
                tuition = tuition + surcharge
        else:
            mandatory = 972
            tuition = (cred_hours * 360) + mandatory
            if diff_cost is True:
                surcharge = (cred_hours * 116)
                tuition = tuition + surcharge

    elif (res_status is False) & (cred_hours >= 12):
        tuition = 17608
        if diff_cost is True:
            tuition = 19008

    elif (res_status is False) & (cred_hours < 12):
        if cred_hours < 9:
            mandatory = 453
            tuition = (cred_hours * 813) + mandatory
            if diff_cost is True:
                surcharge = (cred_hours * 116)
                tuition = tuition + surcharge

        else:
            mandatory = 972
            tuition = (cred_hours * 813) + mandatory
            if diff_cost is True:
                surcharge = (cred_hours * 116)
                tuition = tuition + surcharge
    total = float(tuition)
    return total


if __name__ == '__main__':
    get_user_info()