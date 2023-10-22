DICT = {"kocka":"cat",
        "pes":"dog",
        "mys":"mouse",
        "zralok":"shark"}

czech_word = input()
if czech_word in DICT.keys():
	english_word = DICT[czech_word]
	print(czech_word + " is a " + english_word)
else:
	print("I dont know that word bro.")