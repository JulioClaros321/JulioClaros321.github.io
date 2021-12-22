# Julio Claros
# 114153234
# 2018-05-09
# Assignment: Exercise P4E 5
""" My first function allows for the user to accepts an integer between 10 and 100 within its parameter. If any other
input is put inside then it'll say invalid response and loop with a pls try again method until a valid input is established

Arg 1: number must be a valid integer of at least 10
Arg 2: number must be a valid integer no greater than 100

prints: Your integer input as the established amounts of digits for the next function"""
#def get_integer(lol)

    lol = input()
    number = int(lol)
    while True:
        if number < 10 or number > 100:
            print("invalid response, pls try again")
            number = int(input())
    else:
        print("You have chosen", number, "as your amount of digits")

""" Takes the number that passes the first function's rules and creates an array from 1 to the users input.
Uses a counter to keep track of the size of the array and calculates the total sum and product of all numbers within the
array. 

While Loop: as long as counter, which is currently set as 1, is less then or equal to the users input than keep looping
and adding the counter value in the array space.

For Loop: Iterate through the entire array of values and add/multiple all values accordingly

Print: The array list and total values"""
def greatest(number):
    number = int(number)
    get_integer(number)
    total_sum = 0
    total_product = 1
    counter = 1
    list = []
    while counter <= number:
        list.append(counter)
        counter = counter + 1
    for total in list:
        total_sum = sum(list)
        total_product *= total

    print(list)
    print("Total Sum:", total_sum)
    print("Total Product:", total_product)



if __name__ == '__main__':
    greatest(input())