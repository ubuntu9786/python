ref1 = open("/home/liam/Documents/Code/Python Learning/refs/reference.txt", "r")

print(ref1.readlines()[3])

ref1.close()

ref2 = open("/home/liam/Documents/Code/Python Learning/refs/reference3.txt", "a+")
ref2.write("\n" + input("input something: "))
print(ref2.readable())
print(ref2.read())
ref2.close() 

try:
    ref3 = open("/home/liam/Documents/Code/Python Learning/refs/reference.txt", "a")
    ref3.writelines([input("alight here we go: ")])
    ref3.close()

    ref3 = open("home/liam/Documents/Code/Python Learning/refs/reference.txt")
    print(ref3.read())
except FileNotFoundError as err1:
    print("This file doesnt exist for some reason")
    print(err1)

ref3.close()