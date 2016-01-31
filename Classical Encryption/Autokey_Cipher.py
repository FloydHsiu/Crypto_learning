#Autokey Cipher - Shift and polyalphabetic cipher

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


print ('Please input the text you want to encrypt:')
plain = input()
print ('Please input your key')
key = input()
cipher = Encrypt(key, plain)
print (cipher)

print ('Try Decrypt:' + Decrypt(key, cipher))
