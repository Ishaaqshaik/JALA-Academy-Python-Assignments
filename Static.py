# Define a static variable and access that through a class 

class Student:
    
    schoolcode = 12345

    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"{self.name} belongs to school code: {Student.schoolcode}")

print("School Code:", Student.schoolcode)

s1 = Student("Rahul")
s2 = Student("Priya")

s1.display()
s2.display()