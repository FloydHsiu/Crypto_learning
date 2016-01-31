def Encrypt(key, plain):
	count = 0
	key_len = len(key)
	key = key.upper()
	plain = plain.upper()
	cipher = ''
	for i in plain:
		if i.isalpha():
			cipher = cipher + Xor_alpha(key[count], i)
			count = (count+1)%key_len
	return cipher

#take the alphanet in the plain text to do 'XOR' with key by sequence.

def Xor_alpha(s_key, s_plain):
	p = ord(s_plain) - 65
	k = ord(s_key) - 65
	bin_p = bin(p).replace('0b', '')
	bin_k = bin(k).replace('0b', '')
	cipher = ''
	if len(bin_p) != len(bin_k):
		if len(bin_p) > len(bin_k):
			for i in range(len(bin_k), len(bin_p)):
				bin_k = '0' + bin_k
		else:
			for i in range(len(bin_p), len(bin_k)):
				bin_p = '0' + bin_p
	for i in range(0, len(bin_p)):
		cipher = cipher + str( int(bin_p[i]) ^ int(bin_k[i]) )

	return chr((int(cipher, 2)% 26 + 65))

#this method is case insensitive
#encrypt function also equal to decrypt function

print ('Please input the text you want to encrypt:')
plain = input()
print ('Please input your key')
key = input()
print (Encrypt(key, plain))
