def Encrypt(key, p):
	if p.isalpha():
		if p.islower():
			result = (ord(p)-97+key)%26 + 97
			return (chr(result))
		else:
			result = (ord(p)-65+key)%26 + 65
			return (chr(result))
	else:
		return p
	
def Decrypt(key, p):
        if p.isalpha():
                if p.islower():
                        result = (ord(p)-97+26-key)%26 + 97
                        return (chr(result))
                else:
                        result = (ord(p)-65+26-key)%26 + 65
                        return (chr(result))
        else:
                return p
 
#ord(p): a function which can change str to unicode(number)
#chr(result): a function which can change unicode(number) to str

'''      
f = open('/Users/Floyd/Desktop/test', 'r')
a = f.read()
wf = open('/Users/Floyd/Desktop/crypto', 'w')
for i in a:
	wf.write(Encrypt(1, i))
wf.close()
f.close()

f = open('/Users/Floyd/Desktop/crypto', 'r')
a = f.read()
for i in a:
        print(Decrypt(1, i), end="")
f.close()'''

print ("Input the plain text:")
p = input()
print ("input the key:")
k = input()
if k.isdecimal():
        key = int(k)
        for i in p:
                print(Encrypt(key, i), end="")
else:
        print("You enter wrong key!")








