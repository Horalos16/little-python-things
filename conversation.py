print("Hey :)")
print("What is your name?")
name = input()
if(name == "Andrew"):
    print("Hey I am also Andrew")
else:
    print("Hey", name)

print("How old are you?", name)
age = int(input())
    
if(age >= 0 and age < 6):
    print("Oh, so you are not going to school yet.")
elif(age >= 6 and age < 16):
    grade = age - 5
    print("Oh, so you are going to school and you are in ", grade, "th grade.")
else:
    print("Oh, so you are not going to school anymore")

    
    
    