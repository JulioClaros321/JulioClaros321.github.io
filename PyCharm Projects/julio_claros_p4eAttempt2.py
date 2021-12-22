# Julio Claros
# 114153234
# 2018-05-09
# Assignment: Exercise P4E 5
""" My first function allows for the user to accepts an integer between 10 and 100 within its parameter. If any other
input is put inside then it'll say invalid response and loop with a pls try again method until a valid input is established

Arg 1: if any special character entered, 10 set as ur default counting value
Arg 2: number must be a valid integer of at least 10
Arg 3: number must be a valid integer no greater than 100


Returns: your value as an integer which is used as the parameter for the 2nd function"""

def check_number(number):
    print("Welcome to counting simulator. For ages 3-7!! Lets count up to", number)
    try:
        int(number)
        answer = int(number)
    except ValueError:
        print("This is not a number, value set to 10 as default")
        answer = 10

    while answer < 10 or answer > 100:
        print("invalid response, plz try again")
        answer = int(input())
    return answer

"""The second function takes the return value of the previous function check_number(number) as its parameter n. 

Arg 1: Calls first function with parameter recieved from user input and stores value in variable (limit) which is an
integer value

Variables total_sum, total_product, counter, and List(arrayed) defined and set with default values within the function

While Loop: while counter is less than or equal to (Limit), which is the value of the users input, add a slot in List
array and fill it with the value of counter which is set to 0
- Add 1 to counter and continue loop until counter is = to limit

For Loop: For total amount of values in List[] array, iterate through all the values and add them up, then store them 
in total_sum. Also, as we iterate through the array multiple all values in the array and store value in total_product

Print: Entire array List[]
Print: (prompt)
Print: (prompt) + value of (total_sum)
Print: (prompt) + value of (total_product)

if main: call function def_greatest with value of user input
"""

def greatest(n):
    limit = (check_number(n))
    total_sum = 0
    total_product = 1
    counter = 1
    list = []
    while counter <= limit:
        list.append(counter)
        counter = counter + 1
    for total in list:
        total_sum = sum(list)
        total_product *= total
    print(list)
    print("Now lets add all these numbers together!!")
    print("Total Sum: ", total_sum)
    print("Your pretty smart! How about we multiple them all together!")
    print("Total Product ", total_product)


if __name__ == '__main__':
    greatest(input())