import pyAesCrypt
import os
import re

def encrypt_and_delete(file):
	buffersize=64*1024
	password="hegazy"
	pyAesCrypt.decryptFile(file,file.strip(".hegazy") ,password,buffersize)
	os.remove(file)

files=os.listdir()

for file in files:
	x=re.match('\w+\.\w+\.\w',file)

	if x:
		encrypt_and_delete(file)

