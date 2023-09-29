import time
from colorama import init
from termcolor import colored

init()
greeting = ""
while(True):
	greeting = greeting + "ПРИВЕТ "
	print(colored(greeting, "black", "on_yellow"))
	if(len(greeting)>135):
		greeting = ""		
	time.sleep(0.1)