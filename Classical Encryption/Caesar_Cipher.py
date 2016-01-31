#Caesar Cipher - Shift and monoalphabetic cipher
def Encrypt(key, plain):
        cipher = ''
        for p in plain:
                if p.isalpha():
                        if p.islower():
                                result = (ord(p)-97+key)%26 + 97
                                cipher = cipher + (chr(result))
                        else:
                                result = (ord(p)-65+key)%26 + 65
                                cipher = cipher + (chr(result))
                else:
                        cipher = cipher + p
        return cipher
	
def Decrypt(key, plain):
        cipher = ''
        for p in plain:
                if p.isalpha():
                        if p.islower():
                                result = (ord(p)-97+26-key)%26 + 97
                                cipher = cipher + (chr(result))
                        else:
                                result = (ord(p)-65+26-key)%26 + 65
                                cipher = cipher + (chr(result))
                else:
                        cipher = cipher + p
        return cipher
 
#ord(p): a function which can change str to unicode(number)
#chr(result): a function which can change unicode(number) to str

print ("Input the plain text:")
p = input()
print ("input the key:")
k = input()
if k.isdecimal():
        key = int(k)
        cipher = Encrypt(key, p)
        print (cipher)
        print ('Try Decrypt:' + Decrypt(key, cipher))
else:
        print("You enter wrong key!")








