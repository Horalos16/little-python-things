import sys
import argparse
from typing import Any
from operator import itemgetter, attrgetter, methodcaller
import random
import keyboard
#import yaml

if __name__ == "__main__":
    secret_number = random.randint(0,20) 
    max_attempts = 4
    amount_attempts = 0
    limit_number_max = 20
    limit_number_min = 0
    print()     
    print("Dude !!! you have max attempts ", max_attempts, "UNDERSTAND???\n")
    print("the number is 0 - ", limit_number_max)
    print()
    print("If you want to give up submit 'q'\n")
    while True:
        print ("input number")
        input_a = input()
        if (input_a =="b"):
            amount_attempts = amount_attempts -1
            continue             
        print ("warning,you input:", input_a)
        if (input_a =="q"):
            print("Alright the number is ", secret_number)
            exit()
        input_b = int(input_a)
        if (limit_number_max >= input_b and limit_number_min < input_b):     #input_a is between limit_number_min and limit_number_max
            amount_attempts = amount_attempts + 1
            if (amount_attempts > max_attempts):
                print("Too many attempts, bro!!!!!")
                exit()
            else:
                if (secret_number < input_b):
                    print("too much")
                elif (secret_number > input_b):
                    print("too little")
                else: 
                    print("WHAT ARE YOU DOING?!  OH MY GOD!!! YES YES YES")
                    exit() 
        else: 
            print("Read the instructions, bro")
