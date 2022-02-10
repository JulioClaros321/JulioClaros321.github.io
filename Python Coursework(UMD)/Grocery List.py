# Julio Claros
# 114153234
# 2018-29-08
# Assignment: Exercise P4E

'''Currently, I coded a function that calls a script that sorts various items unto a grocery list to avoid having to
remember anything.It is set to prompt, "Welcome to your unique shopping list. What item would you like to add?", if
this is the pain.py file. It currently operates on a while loop to continuously add items/strings to an array
that it'll later print out once you the restrictions on the while loop, which is the answer n or no when you
finished adding items and returns your list to you. I did run into issues with the list.sort() function before printing
because it kept making the while loop continuous. Will look into reworking it so that the list is easier to read once
printed.'''


def grocery_list(item):
    print("Your first item has been added successfully!")
    food_list = []
    food_list.append(item)
    repeat = input("Would you like to add another item? Yes or No/ Y or N? ")

    while repeat.lower() == "y" or repeat.lower() == "yes":
        print("Waiting for next item... ")
        item = input()
        food_list.append(item)
        repeat = input("Would you like to add another item? Yes or No/ Y or N? ")

    print()
    print("Here is your shopping list:")
    for everything in food_list:
        print(everything)


if __name__ == '__main__':
    print("Welcome to your unique shopping list! What food item do you need today?")
    answer = input()
    grocery_list(answe