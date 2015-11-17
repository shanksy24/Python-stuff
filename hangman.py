def print_hangman(score, word, alpha):
	if score == 0:
		print "-------   "
		print "|         "
		print "|         "
		print "|         "
		print "|         "
		print "|         "
		print_alpha(alpha)
	elif score == 1:
		print "-------   "
		print "|     O   "
		print "|         "
		print "|         "
		print "|         "
		print "|         "
		print_alpha(alpha)
	elif score == 2:
		print "-------   "
		print "|     O   "
		print "|   --    "
		print "|         "
		print "|         "
		print "|         "
		print_alpha(alpha)
	elif score == 3:
		print "-------   "
		print "|     O   "
		print "|   -- -- "
		print "|         "
		print "|         "
		print "|         " 
		print_alpha(alpha)
	elif score == 4:
		print "-------   "
		print "|     O   "
		print "|   --|-- "
		print "|     |   "
		print "|         "
		print "|         "
		print_alpha(alpha)
	elif score == 5:
		print "-------   "
		print "|     O   "
		print "|   --|-- "
		print "|     |   "
		print "|    /    "
		print "|   /     "
		print_alpha(alpha)
	elif score == 6:
		print "-------   "
		print "|     O   "
		print "|   --|-- "
		print "|     |   "
		print "|    / \  "
		print "|   /   \ "
		print "You Lose!"
		exit()
	print word

def print_alpha(alpha):
	print "".join(alpha)

new_word = ""
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print "\nLet's play Hangman\n"

true_word = raw_input("Player, enter a word : ")
show_word = ""
show_word_list = []
true_word_list = []
check = 0

score = 0

for turn in range(20):	
	check = 0
	if turn == 0:
		print "Guess ", turn + 1
		guess = raw_input("Your Guess : ")
		alpha.remove(guess)
		last_word = ""
		for l in true_word:
			show_word = show_word + "-"
	else:
		print "Guess ", turn + 1
		guess = raw_input("Your Guess : ")
		alpha.remove(guess)

	if len(guess) > 1:
		while len(guess) > 1:
			print "Guess was too long!"
			print "Guess ", turn + 1
			guess = raw_input("Your Guess : ")
	elif len(guess) < 1:
		while len(guess) < 1:
			print "Guess was too short!"
			print "Guess ", turn + 1
			guess = raw_input("Your Guess : ")
	elif len(guess) == 1:
		for index, l in enumerate(true_word):
			if l != guess:
				check = check + 1
			elif l == guess:
				show_word_list = list(show_word)
				true_word_list = list(true_word)
				show_word_list[index] = true_word_list[index]
				show_word = ''.join(show_word_list)
	if check == len(true_word):
		score = score + 1

	print_hangman(score, show_word, alpha)

	if show_word == true_word:
		print "Congrats! You Guessed it!\nYou Won!"
		exit()

print "You lost!\nBad luck!"
