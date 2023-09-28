import time
greeting = ""
while(True):
	greeting = greeting + "ПРИВЕТ "
	print(greeting)	
	if(len(greeting)>135):
		greeting = ""		
	time.sleep(0.1)