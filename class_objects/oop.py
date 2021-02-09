#classes are objects apparently

# def hello():
#     print("hello")

# x = 1
# print(type("sup"))
# print(type(x))
# print(type(hello))

# # the string.xxxx is a "method"
# string = "hello"
# print(string.upper())

# operations defined under a 'class' are what can be preformed on it. Think + to int 
class dog: 

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    # def add_one(self, x):
    #     return x + 1

    def bark(self):
        print("bark")

d = dog("fluffles", 12)
print(d.get_age())
d.set_age(input("input a new age: "))
print(d.get_age())





# d.bark()
# print(d.add_one(5))
# print(type(d))
# print(d.name)
print