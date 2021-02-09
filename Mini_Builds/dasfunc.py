import random

heather = "dingus"

def roll(num):
    return random.randint(1, num)

def get_filen(filename):
    return filename[filename.index(".") + 1:]


num = int(input("choose a number: "))
def even_odd(num):
    if num%2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
even_odd(num)
