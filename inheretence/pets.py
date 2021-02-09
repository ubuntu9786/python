class pet: 
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def speak(self):
        print("I am a non talking pet yo")

class dog(pet):
    def speak(self):
        print("woof")

class cat(pet):
    def speak(self):
        print("meow i think")

class anaconda(pet):
    pass

d = dog("fluffles", 14)
c = cat("snuggles", 5)
a = anaconda("slither", 100)

a.speak()

