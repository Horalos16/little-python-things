import time
import winsound
from colorama import init
from termcolor import colored

frequency = 2000 # Set Frequency To 2500 Hertz
duration = 150 # Set Duration To 1000 ms == 1 second

counter = 1

print()
print("Alright, this a reaction game. Wait until you hear a beep sound and then press CRTL + C as fast as possible.")
time.sleep(6)
winsound.Beep(frequency, duration)
while(True):
	if(counter	% 100 == 0):
		message = str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter) + " " + str(counter)	
		print(colored(message,  "blue", "on_yellow"))
	elif(counter % 2 == 0):
		print(colored(counter, "blue", "on_light_green"))
			

	else:
		print(counter)
	counter = counter + 1