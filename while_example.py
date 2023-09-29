import time 
from colorama import init
from termcolor import colored

def color_drawing():
	
	init()
	greeting = ""
	while(True):
		greeting = greeting + "ПРИВЕТ "
		print(colored(greeting, "black", "on_yellow"))
		if(len(greeting)>135):
			greeting = ""		
		time.sleep(0.1)

def drawing_limited(): 

	counter = 0

	while(counter < 1000581):
		print(counter)
		counter = counter+1


# ===== main ======
drawing_limited()
#color_drawing()