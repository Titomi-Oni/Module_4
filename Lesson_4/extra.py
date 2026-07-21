#Write a Python program to create a class Student with a private data member marks.
#Initialize the marks to 75 using a constructor.
#Create a method to display the marks and another method to update the marks.
#Demonstrate why the marks cannot be changed directly using the object.

class Student:
    def __init__(self, marks_75):
        self.marks_75 = marks_75
    
    def marks(self):
        print ("Marks",self.marks_75)

    def update(self):
        self.marks_75 = 87
s = Student(80)
s.marks()