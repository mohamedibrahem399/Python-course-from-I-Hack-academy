import os 
import time 

for i in range (20):
	with open ("G:\\New folder6\\"+str(i)+".txt","w") as file:
		file.write(str(i))

	file.close()