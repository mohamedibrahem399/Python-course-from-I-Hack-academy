message ='attack monkeys'

def encript(letter):
	if ord(letter)>=97 and ord(letter)<=122 :
		if ord(letter)>109 :
			encripted_letter=ord(letter)-13
		else:
			encripted_letter=ord(letter)+13
	elif ord(letter)>=65 and ord(letter)<=90 :
		if ord(letter)<77:
			encripted_letter=ord(letter)+13
		else:
			encripted_letter=ord(letter)-13
	return (chr (encripted_letter))

print(encript('y'))
