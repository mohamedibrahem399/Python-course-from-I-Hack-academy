import os 
import time

for i in range (20):
	
	with open ("G:\\New folder\\" + str(i)+".txt","w") as f:
		f.write(str(i))
		f.write("hello,, it is me , do u remember?")

	f.close()
