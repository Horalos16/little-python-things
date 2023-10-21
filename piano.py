import keyboard
import time
import winsound
import random
duration = 150 
NOTE_C = 523
NOTE_E = 659
NOTE_G = 784
NOTE_D = 587
NOTE_F = 698
NOTE_A = 880
NOTE_H = 988
NOTE_H0 = 493
NOTE_GIS = 830

NOTE_C2 = 1047

DURATION_4 = 300
DURATION_8 = int(DURATION_4 / 2)
DURATION_2 = DURATION_4 * 2
DURATION_2D = DURATION_2 + DURATION_4

print("Alright press keys, A, S, D, F, G, H, J, K, L and have fun :D")
print("Or press 1 or 0 to have even more fun (+_+).")
print("Or press tab to play a song. (*_*).")
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
	elif(keyboard.is_pressed("0")):
		for counter in range(20):
			frequency = random.randint(37,1000)
			print("Playing "+str(frequency)) 
			winsound.Beep(frequency, duration)
	elif(keyboard.is_pressed("o")):
		winsound.Beep(NOTE_C, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_G, DURATION_2)
		winsound.Beep(NOTE_C, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_G, DURATION_2)
		winsound.Beep(NOTE_E, DURATION_8)
		winsound.Beep(NOTE_E, DURATION_8)
		winsound.Beep(NOTE_D, DURATION_8)
		winsound.Beep(NOTE_E, DURATION_8)
		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_D, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_8)
		winsound.Beep(NOTE_E, DURATION_8)
		winsound.Beep(NOTE_D, DURATION_8)
		winsound.Beep(NOTE_E, DURATION_8)
		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_D, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_D, DURATION_4)
		winsound.Beep(NOTE_C, DURATION_2)
	elif(keyboard.is_pressed("v")):
		winsound.Beep(NOTE_A, DURATION_2)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_A, DURATION_4)

		winsound.Beep(NOTE_G, DURATION_4)
		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_D, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_H0, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_C, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_A, DURATION_2)
		winsound.Beep(NOTE_GIS, DURATION_4)
		winsound.Beep(NOTE_A, DURATION_4)

		winsound.Beep(NOTE_H, DURATION_4)
		winsound.Beep(NOTE_A, DURATION_4)
		winsound.Beep(NOTE_F, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_C2, DURATION_4)
		winsound.Beep(NOTE_H, DURATION_4)
		winsound.Beep(NOTE_C2, DURATION_4)

		winsound.Beep(NOTE_A, DURATION_2D)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_A, DURATION_2)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_A, DURATION_4)

		winsound.Beep(NOTE_G, DURATION_4)
		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_D, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_H0, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_F, DURATION_4)
		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_C, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_A, DURATION_2)
		winsound.Beep(NOTE_GIS, DURATION_4)
		winsound.Beep(NOTE_A, DURATION_4)

		winsound.Beep(NOTE_H, DURATION_4)
		winsound.Beep(NOTE_A, DURATION_4)
		winsound.Beep(NOTE_F, DURATION_4)
		time.sleep(DURATION_4/1000)

		winsound.Beep(NOTE_E, DURATION_4)
		winsound.Beep(NOTE_C2, DURATION_4)
		winsound.Beep(NOTE_H, DURATION_4)
		winsound.Beep(NOTE_C2, DURATION_4)

		winsound.Beep(NOTE_A, DURATION_2D)
		time.sleep(DURATION_4/1000)
