import keyboard
import time
import winsound
duration = 150 # Set Duration To 1000 ms == 1 second
print("Alright press keys, A, S, D, F, G,  and have fun :D")
while(True):
	time.sleep(0.1)
	if(keyboard.is_pressed("a")):
		winsound.Beep(440, duration)
	elif(keyboard.is_pressed("s")):		
		winsound.Beep(494, duration)
	elif(keyboard.is_pressed("d")):
		winsound.Beep(523, duration)
	elif(keyboard.is_pressed("f")):
		winsound.Beep(659, duration)
	elif(keyboard.is_pressed("g")):
		winsound.Beep(698, duration)
