import time
greeting = ""
while(True):
	greeting = greeting + "AHOJ "
	print(greeting)	
	if(len(greeting)>135):
		greeting = ""		
	time.sleep(0.1)