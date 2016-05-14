#Binary to Text Conversion and visa versa

def Checker (input_string):
	binary_true = True
	for l in input_string:
		if l == '0' or l == '1' or l == ' ':
			pass
		else:
			binary_true = False
			String_To_Binary(input_string)
			break
	if binary_true == True:
		Binary_To_String(input_string)

def Binary_To_String (input_string):
	input_list = input_string.split()
	final_list = []
	for b in input_list:
		final_list.append(chr(int(b, 2)))
	print "\nConversion : "
	print ''.join(final_list), '\n'

def String_To_Binary (input_string):
	print '\n', "Conversion : "
	print ' '.join(format(ord(x), 'b') for x in input_string), '\n'

def main ():
	terminate = False
	while terminate == False:
		input_string = raw_input("\tInput : ")
		if input_string == "Exit" or input_string == "exit" or input_string == "EXIT":
			terminate = True
			break
		Checker(input_string)

main()
