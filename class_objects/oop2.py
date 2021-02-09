class population:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(population): 
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade #between 0 and 100
    
    def get_grade(self):
        return self.grade

class prof(population):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
# this above references the "super class" aka what comes before
    def get_name(self):
        return self.name

class course:
    def __init__(self, name, max_stu, proffesor):
        self.name = name
        self.max_stu = max_stu
        self.proffesor = proffesor
        self.students = []
        

    def add_student(self, student):
        if len(self.students) < self.max_stu:
            self.students.append(student)
            return True
        return False
    
    def get_ave(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)





s1 = student("ding", 21, 95)
s2 = student("wing", 14, 75)
s3 = student("bing", 221, 85)
p1 = prof("Dr doodle", 32, "Science",)

course1 = course("science", 2, p1)
course1.add_student(s1)
course1.add_student(s2)
print(course1.add_student(s3))


print(course1.students[0].name)
print(course1.get_ave)
print(course1.proffesor.name)




