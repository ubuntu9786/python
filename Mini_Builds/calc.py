try:
    num1 = float(input("enter an number yo: "))
    num2 = float(input("enter an other number yo: "))
except ValueError as err:
    print("i said a number")
    print(err)
result = (num1) + (num2)

print (result)