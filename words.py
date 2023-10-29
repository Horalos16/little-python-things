import random
import time
FILE_PATH = 'C:\\Users\\horal\\Documents\\quizlet-sets\\Ondra-german-gtm.csv'
# FILE_PATH = 'C:\\Users\\horal\\Documents\\quizlet-sets\\Vladik-chemicke-prvky.csv'
# FILE_PATH = 'C:\\Users\\horal\\Documents\\quizlet-sets\\Honza-norsk-ord.csv'
def readDictionaryFromFile():

	f = open(FILE_PATH, "r", encoding="utf-8")
	content = f.read()
	f.close()

	wordDict = {}
	lines = content.split('\n')
	for line in lines:
		parts = line.split(',')
		if len(parts) > 1:	
			wordDict[parts[1]] = parts[0]

	return wordDict
   
wordDict = readDictionaryFromFile()

keys = list(wordDict.keys())
german_word = keys[random.randint(0, len(wordDict)-1)]
czech_word = wordDict[german_word]
print(czech_word)
time.sleep(3)
print(german_word)