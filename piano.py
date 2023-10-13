import keyboard
import time
import winsound
import random
duration = 150 # Set Duration To 1000 ms == 1 second
print("Alright press keys, A, S, D, F, G, H, J, K, L and have fun :D")
print("Or press 1 or 2 to have even more fun (+_+) .")
while(True):
	time.sleep(0.1)
	if(keyboard.is_pressed("a")):
		winsound.Beep(440, duration)
	elif(keyboard.is_pressed("s")):		
		winsound.Beep(494, duration)
	elif(keyboard.is_pressed("d")):
		winsound.Beep(37, duration)
	elif(keyboard.is_pressed("f")):
		winsound.Beep(659, duration)
	elif(keyboard.is_pressed("g")):
		winsound.Beep(698, duration)
	elif(keyboard.is_pressed("h")):
		winsound.Beep(736, duration)
	elif(keyboard.is_pressed("j")):
		winsound.Beep(775, duration)
	elif(keyboard.is_pressed("k")):
		winsound.Beep(812, duration)
	elif(keyboard.is_pressed("l")):
		winsound.Beep(852, duration)
	elif(keyboard.is_pressed("1")):
		frequency = random.randint(37,1000) 
		winsound.Beep(frequency, duration)
	elif(keyboard.is_pressed("2")):
		for counter in range(20):
			frequency = random.randint(37,1000)
			print("Playing "+str(frequency)) 
			winsound.Beep(frequency, duration)