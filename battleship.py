from random import randint

def print_board(board):
	print "\n    1 2 3 4 5"
	print "    | | | | |"
	for index, row in enumerate(board):
		print index + 1, "-",
		print " ".join(row)
	print "\n"

def random_row(limit):
	return randint(1, limit)

def random_col(limit):
	return randint(1, limit)

def col_guess_func():
	return int(raw_input("Enter Column Guess : "))

def row_guess_func():
	return int(raw_input("Enter Row Guess : "))

board = []
ship_row = random_row(5)
ship_col = random_col(5)

for n in range(5):
	board.append(["O"] * 5)

print "\nLet's play battleship!\n"
moves = int(raw_input("How many moves do you want? : "))

for turn in range(moves):
	print "\nTurn ", turn + 1
	print_board(board)

	col_guess = col_guess_func()
	row_guess = row_guess_func()

	if col_guess not in range(1, 6) or row_guess not in range(1, 6):
		while col_guess not in range(1, 6) or row_guess not in range(1, 6):
			print "\nYour guess was invalid.\nPlease enter again.\n"
			col_guess = col_guess_func()
			row_guess = row_guess_func()


	if board[row_guess - 1][col_guess - 1] == "X":
		while board[row_guess - 1][col_guess - 1] == "X":
			print "\nYou already guessed that!\nGuess again.\n"
			col_guess = col_guess_func()
			row_guess = row_guess_func()

	if col_guess == ship_col and row_guess == ship_row:
		print "\nYou sank my battleship!\n"
		exit()

	else:
		board[row_guess - 1][col_guess - 1] = "X"
        print "\nWrong!"

print "You have run out of turns!\nYou lose!"
print "\nThe ship (~) was actually at row %s and col %s." % (ship_col, ship_row)
board[ship_col - 1][ship_row - 1] = "~"
print_board(board)
