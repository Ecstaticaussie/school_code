from random import random, randint
from math import trunc
from copy import copy, deepcopy

initial_2d = [[None for i in range(3)] for i in range(3)]
hex_dict = {"0":"0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}

def ioutput():
    for row in initial_2d: print(row)

def routput():
    for row in final_2d: print(row)

def bin_converter(num):
    int_num = trunc(num)
    bin_int = bin(int_num)[3:]
    decimal_num = int((int_num - num) * 1000)
    bin_decimal = "000" if bin(decimal_num)[3:6] == "" else bin(decimal_num)[3:6]
    return f"{bin_int}.{bin_decimal}"

for i in range(3):
    for j in range(3):
        decision = randint(1, 3)
        match decision:
            case 1: initial_2d[i][j] = randint(-255, 255) + round(random(), 3) #decimal
            case 2: initial_2d[i][j] = "h" + hex(randint(0, 4095))[2:].upper() #hex
            case 3: initial_2d[i][j] = bin_converter(randint(-255, 255) + round(random(), 3)) #binary

final_2d = initial_2d.deepcopy()

for i in range(3):
    for j in range(3):
        num = final_2d[i][j]
        if type(num) == float: #decimal
            pass
        elif num[0] == "h": #hex
            hex_num = num[1:]
            if len(hex_num) == 1: final_2d[i][j] = int(hex_dict[hex_num]) #one hex place
            elif len(hex_num) == 2: final_2d[i][j] = int(hex_dict[hex_num[0]]) * 16 + int(hex_dict[hex_num[1]]) #two hex places
            else: final_2d[i][j] = int(hex_dict[hex_num[0]]) * 256 + int(hex_dict[hex_num[1]]) * 16 + int(hex_dict[hex_num[2]]) #three hex places


        else: #binary
            pass

ioutput()
routput()