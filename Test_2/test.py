student = {"Titomi":90,"Davis":100,"Ren":90,"Sky":100}
sum = 0
for i in student.values():
    sum = sum+i
average = sum / 5
print (average)
max = 0
for i in student.values():
    if max < i:
        max = i
print ("Maximum value is: ",max)

min = 0
for i in student.values():
    if min > i:
        min = i
print ("Minimum value is: ",min)

 
print (student.get("Titomi"))

student_name = input("Please Enter Your Name: ")