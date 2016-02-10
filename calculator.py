#Calculator
from Tkinter import *

root = Tk()



def str_to_int(string_input):
	int_output = 0
	
	for l in string_input:
		int_output = int_output * 10 + int(l)
	return int_output

def Evaluate():
	global equation
	global current_num

	int1 = 0
	int2 = 0
	str1 = ""
	str2 = ""
	first_check = False
	current_op = ""
	op_count = 0

	print equation

	for n in equation:
		if n in op_list:
			op_count += 1

	if op_count >= 2:
		
		for n in equation:
			if n in op_list:
				first_check = True
				current_op = n
				print "op success"
			elif (n in num_list) and first_check == False:#High and Low op_list prioritisation
				str1 += n
				print "first num success"
			elif (n in num_list) and (first_check == True):
				str2 += n
				print "second num success"
			else:
				print "Fail"

	elif op_count == 1:
		for n in equation:
			
			print "`", n

			if n in op_list:
				first_check = True
				current_op = n
				print "op success"
			elif (n in num_list) and first_check == False:
				str1 += n
				print "first num success"
			elif (n in num_list) and (first_check == True):
				str2 += n
				print "second num success"
			else:
				print "Fail"

			print "str1 = ", str1
			print "str2 = ", str2

			int1 = str_to_int(str1)
			int2 = str_to_int(str2)

			float1 = float(int1)
			float2 = float(int2)
			
		if current_op == '+':
			ouput_field["text"] = float1 + float2
		elif current_op == '-':
			ouput_field["text"] = float1 - float2
		elif current_op == '*':
			ouput_field["text"] = float1 * float2
		elif current_op == '/':
			ouput_field["text"] = float1 / float2

		equation = ""
		current_num = 0


def input_num(number):
	global current_num
	
	current_num *= 10
	current_num += number

	print current_num
	
	ouput_field["text"] = current_num

def input_num_1 ():
	input_num(1)

def input_num_2 ():
	input_num(2)

def input_num_3 ():
	input_num(3)

def input_num_4 ():
	input_num(4)

def input_num_5 ():
	input_num(5)

def input_num_6 ():
	input_num(6)

def input_num_7 ():
	input_num(7)

def input_num_8 ():
	input_num(8)

def input_num_9 ():
	input_num(9)

def input_num_0 ():
	input_num(0)

def input_num_add():
	global equation
	global current_num

	equation = equation + (str(current_num) + "+")
	print equation
	current_num = 0

def input_num_sub():
	global equation
	global current_num

	equation = equation + (str(current_num) + "-")
	print equation
	current_num = 0

def input_num_mul():
	global equation
	global current_num

	equation = equation + (str(current_num) + "*")
	print equation
	current_num = 0

def input_num_div():
	global equation
	global current_num

	equation = equation + (str(current_num) + "/")
	print equation
	current_num = 0

def input_num_clr():
	global equation
	global current_num

	equation = ""
	current_num = 0

	ouput_field["text"] = current_num

def input_num_equals():
	global equation
	global current_num

	equation = equation + (str(current_num))
	print equation
	Evaluate()
	current_num = 0

first_num = False
current_num = 0
equation = ""
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
op_list = ['+', '-', '*', '/']
high_op_list = ['*', '/']
low_op_list = ['+', '-']

ouput_field = Label(root, text = int(current_num))
pad_1 = Button(root, text = "1", command = input_num_1)
pad_2 = Button(root, text = "2", command = input_num_2)
pad_3 = Button(root, text = "3", command = input_num_3)
pad_4 = Button(root, text = "4", command = input_num_4)
pad_5 = Button(root, text = "5", command = input_num_5)
pad_6 = Button(root, text = "6", command = input_num_6)
pad_7 = Button(root, text = "7", command = input_num_7)
pad_8 = Button(root, text = "8", command = input_num_8)
pad_9 = Button(root, text = "9", command = input_num_9)
pad_0 = Button(root, text = "0", command = input_num_0)
pad_add = Button(root, text = "+", command = input_num_add)
pad_sub = Button(root, text = "-", command = input_num_sub)
pad_mul = Button(root, text = "*", command = input_num_mul)
pad_div = Button(root, text = "/", command = input_num_div)
pad_clr = Button(root, text = "C", command = input_num_clr)
equals = Button(root, text = "=          ", command = input_num_equals)

ouput_field.grid(row = 0, column = 0, columnspan = 3)
pad_1.grid(row = 1, column = 0)
pad_2.grid(row = 1, column = 1)
pad_3.grid(row = 1, column = 2)
pad_4.grid(row = 2, column = 0)
pad_5.grid(row = 2, column = 1)
pad_6.grid(row = 2, column = 2)
pad_7.grid(row = 3, column = 0)
pad_8.grid(row = 3, column = 1)
pad_9.grid(row = 3, column = 2)
pad_0.grid(row = 4, column = 2)
pad_add.grid(row = 1, column = 3)
pad_sub.grid(row = 2, column = 3)
pad_mul.grid(row = 3, column = 3)
pad_div.grid(row = 4, column = 3)
pad_clr.grid(row = 0, column = 3)
equals.grid(row = 4, column = 0, columnspan = 2)

print current_num

root.mainloop()
