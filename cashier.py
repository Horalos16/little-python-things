
print("Tell me how many 1kc does Ondra have.")
ondra_1_kc = int(input())
print("Tell me how many 1kc does Vlada have.")
vlada_1_kc = int(input())
print("Tell me how many 1kc do we have in common.")
common_1_kc = int(input())
total_1_kc = ondra_1_kc + vlada_1_kc + common_1_kc
ammount_1_kc = total_1_kc
print(ammount_1_kc)

print("Tell me how many 2kc does Ondra have.")
ondra_2_kc = int(input())
print("Tell me how many 2kc does Vlada have.")
vlada_2_kc = int(input())
print("Tell me how many 2kc do we have in common.")
common_2_kc = int(input())
total_2_kc = ondra_2_kc + vlada_2_kc + common_2_kc
ammount_2_kc = total_2_kc * 2
print(ammount_2_kc)

print("Tell me how many 5kc does Ondra have.")
ondra_5_kc = int(input())
print("Tell me how many 5kc does Vlada have.")
vlada_5_kc = int(input())
print("Tell me how many 5kc do we have in common.")
common_5_kc = int(input())
total_5_kc = ondra_5_kc + vlada_5_kc + common_5_kc
ammount_5_kc = total_5_kc * 5
print(ammount_5_kc)

print("Tell me how many 10kc does Ondra have.")
ondra_10_kc = int(input())
print("Tell me how many 10kc does Vlada have.")
vlada_10_kc = int(input())
print("Tell me how many 2kc do we have in common.")
common_10_kc = int(input())
total_10_kc = ondra_10_kc + vlada_10_kc + common_10_kc
ammount_10_kc = total_10_kc * 10
print(ammount_10_kc)


print("Tell me how many 20kc does Ondra have.")
ondra_20_kc = int(input())
print("Tell me how many 20kc does Vlada have.")
vlada_20_kc = int(input())
print("Tell me how many 20kc do we have in common.")
common_20_kc = int(input())
total_20_kc = ondra_20_kc + vlada_20_kc + common_20_kc
ammount_20_kc = total_20_kc * 20
print(ammount_20_kc)

print("Tell me how many 50kc does Ondra have.")
ondra_50_kc = int(input())
print("Tell me how many 50kc does Vlada have.")
vlada_50_kc = int(input())
print("Tell me how many 50kc do we have in common.")
common_50_kc = int(input())
total_50_kc = ondra_50_kc + vlada_50_kc + common_50_kc
ammount_50_kc = total_50_kc * 50
print(ammount_50_kc)
				

ondra_ammount = ondra_1_kc + ondra_2_kc * 2 + common_1_kc / 2 + common_2_kc + ondra_5_kc * 5 + ondra_10_kc * 10 + common_5_kc * 5 / 2 + common_10_kc * 10 / 2 + ondra_20_kc * 20 + ondra_50_kc * 50 + common_20_kc * 20 / 2 + common_50_kc * 50 / 2
print("Ondra gets " + str(ondra_ammount)) 
vlada_ammount = vlada_1_kc + vlada_2_kc * 2 + common_1_kc / 2 + common_2_kc + vlada_5_kc * 5 + vlada_10_kc * 10 + common_5_kc * 5 / 2 + common_10_kc * 10 / 2 + vlada_20_kc * 20 + vlada_50_kc * 50 + common_20_kc * 20 / 2 + common_50_kc * 50 / 2
print("Vlada gets " + str(vlada_ammount))
total_ammount_1 = ondra_ammount + vlada_ammount
total_ammount_2 = ammount_1_kc + ammount_2_kc + ammount_5_kc + ammount_10_kc + ammount_20_kc + ammount_50_kc
print(total_ammount_1," ", total_ammount_2)



				# 1 kc = 99
				# 2 kc  = 284
				# 5 kc = 420
				# 10 kc = 480
				# 20 kc = 720
				# 50 kc = 1000