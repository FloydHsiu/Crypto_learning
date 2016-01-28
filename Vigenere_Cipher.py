import tkinter as tk
from tkinter import filedialog 

def Encrypt(key, plain):
	count = 0
	key_len = len(key)
	key = key.upper()
	plain = plain.upper()
	p = ""
	for i in plain:
		if i.isalpha():
			shift = ord(key[count]) - 65
			temp = (ord(i)-65+shift)%26 + 65
			p = p + chr(temp)
			count = (count+1)%key_len
	return p

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

f = open(file_path, "r")
plain_text = f.read()
print ("Please input the key")
key = input()
print (Encrypt(key, plain_text))