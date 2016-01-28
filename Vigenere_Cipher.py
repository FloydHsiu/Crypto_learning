import tkinter as tk
from tkinter import filedialog 

# key is a word, ex: "ABC"
def Encrypt(key, plain):
	count = 0
	key_len = len(key)
	key = key.upper()
	plain = plain.upper()
	cipher = ""
	for i in plain:
		if i.isalpha():
			shift = ord(key[count]) - 65
			temp = (ord(i)-65+shift)%26 + 65
			cipher = cipher + chr(temp)
			count = (count+1)%key_len
	return cipher

def Decrypt(key, cipher):
	count = 0
	key_len = len(key)
	key = key.upper()
	cipher = cipher.upper()
	plain = ''
	for i in cipher:
		if i.isalpha():
			shift = ord(key[count]) - 65
			temp = (ord(i)-65-shift+26)%26 + 65
			plain = plain + chr(temp)
			count = (count+1)%key_len
	return plain

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

f = open(file_path, "r")
plain_text = f.read()
print ("Please input the key")
key = input()
print (Encrypt(key, plain_text))