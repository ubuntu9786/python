class student: 

    def __init__(self, name, major, gpa, probation):
        self.name = name
        self.major = major
        self.gpa= gpa
        self.probation = probation
# You can add functions in classes as shown below   
    def honor(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# class profs:
    
#     def __init__(self, name, profession, exp, tenyear):
#         self.name = name
#         self.profession = profession
#         self.exp = exp
#         self.tenyear = tenyear
