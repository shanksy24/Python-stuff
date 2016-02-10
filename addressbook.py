from sys import argv

script, filename = argv

print "File : ", filename

def GetAllContacts():
	txt = open(filename,'r')

	foo = txt.read()

	txt.close

	fooword = foo.split()

	print '\n'

	for l in fooword:
		temp = str(l)
		foobarword = temp.split(':')

		print ' '.join(foobarword)

	print '\n'


def GetContact(name):
	list_of_suggestions = []
	txt = open(filename, 'r')
	
	text_chunk = txt.read()

	txt.close

	foo = text_chunk.split()

	for l in foo:
		temp = str(l).split(':')

		for t in temp:
			if t == name:
				list_of_suggestions.append(temp)

	for s in list_of_suggestions:
		print '\n', ' '.join(s)


def AddContact(first_name, last_name, number):
	txt = open(filename, 'a')

	txt.write(first_name)
	txt.write(":")
	txt.write(last_name)
	txt.write(":")
	txt.write(number)
	txt.write('\n\n')

	txt.close

	print "\nSuccess\n"


def RemoveContact(name):
	list_of_suggestions = []
	new_text_list = []

	txt = open(filename, 'r')
	
	text_chunk = txt.read()

	txt.close

	foo = text_chunk.split()

	for l in foo:
		temp = str(l).split(':')
		new_text_list.append(l)
		for t in temp:
			if t == name:
				list_of_suggestions.append(l)

	new_text = ""
	new_text = list_of_suggestions[0]

	for index, item in enumerate(new_text_list):
		if item == new_text:
			new_text_list.pop(index)
	
	new_final = ""

	for item in new_text_list:
		new_final += item + "\n"
	
	txt = open(filename, 'w')
	txt.write(new_final)
	txt.close

	print "\nSuccess\n"

while True:
	print "\nWhat would you like to do?\n1) View list of all contacts\n2) View specific contact\n3) Add a contact\n4) Remove a contact"
	choice = int(raw_input("Choice : "))

	if choice == 1:
		GetAllContacts()

	elif choice == 2:
		name = raw_input("\nEnter First or Last Name : ")

		GetContact(name)

	elif choice == 3:
		first_name = raw_input("First Name : ")
		last_name = raw_input("Last Name : ")
		number = raw_input("Number : ")
		AddContact(first_name, last_name, number)

	elif choice == 4:
		name = raw_input("Enter First or Last Name : ")

		RemoveContact(name)

	else:
		"Invalid answer"

