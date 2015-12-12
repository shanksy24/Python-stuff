#Demonstrates of to use a class with Tkinter
from Tkinter import *

class Application(Frame):
	"""A GUI Application with 3 buttons"""
	def __init__(self, master):
		"""Initialise the frame"""
		Frame.__init__(self, master)
		self.grid()
		self.button_clicks = 0 #Counts num of button clicks
		self.creates_widgets()

	def creates_widgets(self):
		"""Create buttons which displays number of clicks"""
		#Create button 
		self.button = Button(self)
		self.button["text"] = "Total clicks = 0"
		self.button["command"] = self.update_count
		self.button.grid()

	def update_count(self):
		"""Increase the click count and display new total"""
		self.button_clicks += 1
		self.button["text"] = "Total clicks = " + str(self.button_clicks)

root = Tk()
root.title("Lazy Buttons")
root.geometry("200x100")

app = Application(root)

root.mainloop()
