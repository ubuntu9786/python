# class attributes are specific to a class not an object

class person: 
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        person.add_person()
# calls on the class itself, not on the instance. good to change class attributes   
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people()

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = person("tim")
p2 = person("John")
print(person.number_of_people_())

