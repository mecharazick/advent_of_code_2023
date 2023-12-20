from os import stat
from re import sub
import sys
import threading

ONE = "one"
TWO = "two"
THREE = "three"
FOUR = "four"
FIVE = "five"
SIX = "six"
SEVEN = "seven"
EIGHT = "eight"
NINE = "nine"

dec_nums = ["1","2","3","4","5","6","7","8","9"]

cursive_nums = [ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]

def main():
    if len(sys.argv) < 2:
        print("Missing arguments")
        exit(-1)
    path = get_file_path(get_args(sys.argv))     
    (f, size) = get_file(path)
    acum = 0
    line = f.readline()
    while line:
        acum += clean_calibration(line, dec_nums)
        line = f.readline()
    f.close()
    print(acum)

def get_args(arg_list):
    return arg_list[1:]

def get_file_path(args):
    return str(args[0])

def get_file(path):
    try:
        f = open(path, 'r')
        size = stat(path).st_size
        print("Found file at " + path)
        return (f, size)
    except:
        print("File does not exist")
        exit(-1)

def clean_calibration(poluted_calibration, calibration_params):
    occur = 0
    first_num = b''
    last_num = b''
    string = sanitize_string(poluted_calibration)
    for char in list(string):
        if char not in calibration_params:
            continue
        if first_num:
            last_num = char
        else:
            first_num = char
    if not first_num:
        return 0
    else:
        if not last_num:
            return char_to_num(first_num + first_num)
        return char_to_num(first_num + last_num)

def sanitize_string(string):
    sanitized_string = string
    word_buff = ""
    temp = ""
    for letter in list(string):
        temp += letter
        for word in cursive_nums:
            num = word_to_num(word)
            word_buff = temp
            temp = temp.replace(word, num)
            if not word_buff.__eq__(temp):
                temp += letter
    print(temp)
    return temp

def word_to_num(word):
    if ONE.__eq__(word):
        return "1"
    elif TWO.__eq__(word):
        return "2"
    elif THREE.__eq__(word):
        return "3"
    elif FOUR.__eq__(word):
        return "4"
    elif FIVE.__eq__(word):
        return "5"
    elif SIX.__eq__(word):
        return "6"
    elif SEVEN.__eq__(word):
        return "7"
    elif EIGHT.__eq__(word):
        return "8"
    elif NINE.__eq__(word):
        return "9"
    else:
        return word

def char_to_num(string):
    return int(string)

main()
