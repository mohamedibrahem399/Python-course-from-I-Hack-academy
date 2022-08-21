import os
count =0
os.mkdir('C:\\Users\\Assem\\Downloads\\test')
path = "C:\\Users\\Assem\\Downloads\\test\\"
while count < 1000:
	count += 1
	os.mkdir(str(count))