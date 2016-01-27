import tkinter as tk
from tkinter import filedialog, Canvas, Frame, BOTH, Tk, Button

def alpha_to_num(x):
	if x.isalpha():
		if x.islower():
			return (ord(x) - 97)
		else:
			return (ord(x) - 65)
	else:
		return -1

class Example(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.initUI()

	def initUI(self):

		self.parent.title("test")
		self.pack(fill=BOTH, expand=1)

		self.cal = Button(self)
		self.cal["text"] = "Calculate"
		self.cal["command"] = self.cal_frequency
		self.cal.pack(fill=BOTH, expand=1)

	def cal_frequency(self):
		# use the dialog to find the route of the file
		file_path = filedialog.askopenfilename()
		frequency = [ 0 for i in range(26)]
		f = open(file_path, 'r')
		article = f.read()
		for i in article:
			seq = alpha_to_num(i)
			if seq != -1:
				frequency[seq] += 1
		print (frequency)

root = Tk()
ex = Example(root)
root.mainloop()





