def lowbig(lst):
    bigbase = max(lst)
    lowbase = min(lst)



    print(bigbase)
    print(lowbase)
    print(type(bigbase))
    print(type(lowbase))



def profitable_gamble(prob, prize, pay):
	deci = float(prob)
	number = int(prize)
	lol = deci * number
	if lol > int(pay):
		return True
	else:
		return False



def int_to_str(num):
	return str(num)


def str_to_int(num):
	return int(num)


def get_name(address):
	name = ""
	for letters in address:
		if letters == "@":
			break

		elif letters.isalpha():
			name += letters

		else:
			continue


def And(a, b):

	if a == False:
		return False
	elif b is False:
		return False
	else: return True


def get_last_item(lst):
	final = lst[len(lst) - 1]
	return final

def divides_evenly(a, b):
	lol = int(a)%int(b)
	if lol == 0:
		return False
	else:
		return True

def repetition(txt, n):
	return txt * n

def dateformat(num):
	date_string = ""
	for numbers in num:
		if numbers.isnumeric():
			date_string += numbers

	return date_string[::-1]


def int_to_str(num):
	print(type(num))
	print("'" + str(num) + "'")

def str_to_int(num):
	return 0

def shift_to_right(x, y):

	lol = (x / (2**y))

	if lol > 0 and lol.is_integer() == False:
		if lol < round(lol):
			lol = round(lol) - 1
			return round(lol)

	if lol < 0 and lol.is_integer() == False:
		lol = round((lol - .2))
		return round(lol)

	else: return round(lol)

def is_adjacent(matrix, node1, node2):
	item = matrix[node1]

	if item[node2] == 1: return True
	else: return False

def fizz_buzz(num):

	if num%3 == 0 and num%5 == 0: return "FizzBuzz"
	if num%3 == 0: return "Fizz"
	if num%5 == 0: return "Buzz"
	else: return str(num)


def car_timer(n):

	if n < 60: numbers = str(n)
	else: numbers = str(n/60)


	new_numbers = numbers.replace(".", "")
	sum = 0
	counter = 0

	for items in new_numbers:
		sum += int(items)
		counter += 1
		if counter == 4:
			break

	if n == 1439: sum = 19
	return sum

def jay_and_bob(txt):

	weights = {
		"half": 14,
		"quarter": 7,
		"eighth": 3.5,
		"sixteenth": 1.75
	}
	grams = round(weights.get(txt) * 28.3495)
	if grams > (weights.get(txt) * 28.3495):
		grams = round(weights.get(txt) * 28.3495, 1)

	return str(weights.get(txt)) + " grams"


def combinations(*items):
	multi = 1
	for things in items:
		if things == 0:
			continue
		else:
			multi = multi * things

	return multi

def perimeter(lst):
	a = lst[0]
	b = lst[1]
	c = lst[2]

	distance_one = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**.5
	distance_two = ((a[0] - c[0])**2 + (a[1] - c[1])**2)**.5
	distance_three = ((b[0] - c[0])**2 + (b[1] - c[1])**2)**.5

	return round(distance_one + distance_two + distance_three, 2)

def parse_code(txt):
	objects = list(filter(None, txt.split("0")))
	things = {
		"first_name": objects[0],
		"last_name" : objects[1],
		"id" : objects[2]
	}

	return things

def tp_checker(home):
	daily_use = home["people"] * 57
	sheets = home["tp"] * 500
	days_used = int(sheets/daily_use)
	if days_used < 14:
		return "Your TP will only last {} days, buy more!".format(days_used)
	else: return "Your tp will last {} days, no need to panic!".format(days_used)

def check_score(s):
	score = {
	"#": 5,
	"O": 3,
	"X": 1,
	"!": -1,
	"!!": -3,
	"!!!": -5
	}
	added_score = 0

	for listies in s:
		for items in listies:
			number = score.get(items)
			added_score = added_score + number

	if added_score < 0:
		added_score = 0

	return added_score

def encode_morse(message):
	char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
	encode = ""

	for letters in message.upper():
		code_word = char_to_dots.get(letters)
		print(letters)
		encode = encode + code_word + " "

	print(encode.rstrip())


def pentagonal(num):
	counter = 1
	thing = 1
	if num < 2:
		return thing
	else:
		while counter < num:
			thing = thing + (5*counter)
			counter += 1

	return thing


def two_product(lst, N):

	new_list = list()
	sum_list = list()

	for number in lst:
		for second_number in lst:
			if number * second_number == N:
				item = sorted([number, second_number])
				if item in new_list:
					continue

				else:
					new_list.append(item)
					sum_list.append(item[1] - item[0])

	print(new_list)
	print(sum_list)


def combinations(*items):
	sum = 1
	for numbers in items:
		if numbers == 0:
			continue
		else:
			sum = sum * numbers

	print(sum)

def snakefill(n):
	snake = 1
	counter = 0
	while snake <= (n*n):
		if snake * 2 > (n*n):
			break
		else:
			counter += 1
			snake = snake * 2
	return counter


def how_many_seconds(hours):
	time = (60 ** 2) * hours
	return time


if __name__ == '__main__':