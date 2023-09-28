print("Give me things you wanna buy.")
shopping_list = []
while True:
	item_1 = input()
	if(item_1 == "quit"):
		break 
	else:
		shopping_list.append(item_1)
print("You want to buy ", shopping_list, ".")