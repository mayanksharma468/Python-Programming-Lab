def students(rollno):
    name=input('enter student name')
    if name in rollno:
         return 'present'
    else:
        return 'absent'
rollno=eval(input('enter the name of student'))
print(students(rollno))
