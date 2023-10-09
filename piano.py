import keyboard
import time
import winsound
frequency =440 # Set Frequency To 2500 Hertz
duration = 150 # Set Duration To 1000 ms == 1 second

while(True):
	time.sleep(0.1)
	if(keyboard.is_pressed("a")):
		winsound.Beep(frequency, duration)
	elif(keyboard.is_pressed("s")):		
		winsound.Beep(523, duration)
