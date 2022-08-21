message ='attack monkeys'

def encript(letter):
	

	if ord(letter)>=97 and ord(letter)<=122 :
		if ord(letter)>109 :
			encripted_letter=chr(ord(letter)-13)
		else:
			encripted_letter=chr (ord(letter)+13)
	elif ord(letter)>=65 and ord(letter)<=90 :
		if ord(letter)<77:
			encripted_letter=chr (ord(letter)+13)
		else:
			encripted_letter=chr(ord(letter)-13)
	else :
		encripted_letter=letter

	return (encripted_letter)

encripted_message=[]

for i in message:
	encripted_letter=encript(i)
	encripted_message.append(encripted_letter)

encript_string=''.join(encripted_message)
print(encript_string)
