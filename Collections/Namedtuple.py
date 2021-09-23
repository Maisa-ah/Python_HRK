from collections import namedtuple
n = int(input())
spreadsheet = input().split()
Student = namedtuple('Student', spreadsheet)
total = 0
for _ in range(n):
    s1,s2,s3,s4 = input().split()
    new_student = Student(s1,s2,s3,s4)
    total = total + int(new_student.MARKS)
total = "{:.2f}".format(total/n)
print(total)
    