import tkinter as tk
from tkinter import filedialog

def Encrypt(key, plain):
	count = 0
	key_len = len(key)
	key = key.upper()
	plain = plain.upper()
	cipher = ''
	autokey = ''
	for i in plain:
		if i.isalpha():
			autokey = autokey + i
			shift = ord(key[count]) - 65
			temp = (ord(i)-65+shift)%26 + 65
			cipher = cipher + chr(temp)
			count = (count+1)%key_len
			if count== 0:
				key = autokey
				autokey = ''
	return cipher

def Decrypt(key, cipher):
	count = 0
	key_len = len(key)
	key = key.upper()
	cipher = cipher.upper()
	plain = ''
	autokey = ''
	for i in cipher:
		if i.isalpha():
			shift = ord(key[count]) - 65
			temp = (ord(i)-65-shift+26)%26 + 65
			plain = plain + chr(temp)
			autokey = autokey + chr(temp)
			count = (count+1)%key_len
			if count== 0:
				key = autokey
				autokey = ''
	return plain


root = tk.Tk()
root.withdraw()
#file_path = filedialog.askopenfilename()

#f = open(file_path, 'r')
print( Encrypt('deceptive', 'wearediscoveredsaveyourself') )
