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
print("Give me a word so I can transalate it to morse code.")
word = input()
morse_message = ""
for char in word:
    morse_char = MORSE_CODE[char]
    morse_message = morse_message + morse_char + "|"

print(morse_message)