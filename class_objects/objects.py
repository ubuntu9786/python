from class1 import student
# from class1 import profs

student1 = student("heather", "wombology", 4.9, True)
student2 = student("liam", "wombology", 2, False)

# pro1 = profs("dr. ding", "wombology", 18, True)

prob = input("show student status? (y or n) ")
if prob == "y":
    print(student1.name)
    print(student1.probation)
else:
    print('')

response = input("would you like to see GPA? (y or n) ")
# reponse = srt(response)

if response == "y":
    print(student1.gpa)
else:
    print('pfft')

print(student1.honor())
print(student2.honor())