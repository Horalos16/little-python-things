import winsound
import time
MORSE_CODE = {"a" : ".-",
              "b" : "-...",
              "c" : "-.-.",
              "d" : "-..", 
              "e" : ".",
              "f" : "..-.",
              "g" : ".-.",
              "h" : "....",
              "ch" : "----",
              "i" : "..",
              "j" : ".---",
              "k" : "-.-",
              "l" : ".-..",
              "m" : "--",
              "n" : "-.",
              "o" : "---",
              "p" : ".--.",
              "q" : "--.-",
              "r" : ".-.",
              "s" : "...",
              "t" : "-",
              "u" : "..-",
              "v" : "...-",
              "w" : ".--",
              "x" : "-..-",
              "y" : "-.--",
              "z" : "--..",}
frequency = 590
LONG_SOUND = 700
SHORT_SOUND = 250
print("Give me a word so I can transalate it to morse code.")
word = input()
morse_message = ""
for char in word:
    morse_char = MORSE_CODE[char]
    morse_message = morse_message + morse_char + "|"
print(morse_message)

for char in morse_message:
    if(char == "."):
        winsound.Beep(frequency, SHORT_SOUND)
    elif(char == "-"):
        winsound.Beep(frequency, LONG_SOUND)
    elif(char == "|"):
        time.sleep(1.5)