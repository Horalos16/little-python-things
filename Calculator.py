
print("Alright I am your calculator, give me first number, an operator and second number. \n")
first_number = int(input())
operator = input()
second_number = int(input())
result = first_number + second_number
result_1 = first_number - second_number
result_2 = first_number * second_number
result_3 = first_number / second_number
if(operator == "-"):    
	print(first_number, "-", second_number, "=", result_1)
elif(operator == "+"):
    print(first_number, "+", second_number, "=", result)
elif(operator == "*"):
    print(first_number, "*", second_number, "=", result_2)
elif(operator == "/"):
	print(first_number, "/", second_number, "=", result_3)
else:
	print("Sorry bro these are not numbers.")