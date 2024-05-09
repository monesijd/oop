class Student:
    
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def bmi(self):
        return self.weight / (self.height / 100.0) ** 2

    def is_fat(self):
        if self.bmi() >= 35:
            return True
        else:
            return False

students = [
        Student('Bill', 169, 100),        
        Student('Brian', 164, 56),
        Student('Eagle', 173, 20)
]

for student in students:
    if student.is_fat():
        print(student.name)
