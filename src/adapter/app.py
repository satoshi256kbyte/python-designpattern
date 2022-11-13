"""
Adapterパターン
"""

from student import Student
from reiwa_student import ReiwaStudent

student1: Student = Student(30, 'AA', 'BB')
student2: ReiwaStudent = ReiwaStudent(30, 'CC', 'DD')
student3: ReiwaStudent = ReiwaStudent(4, 'EE', 'FF')
student4: ReiwaStudent = ReiwaStudent(2023, 'GG', 'HH')
print(student1.code())
print(student2.code())
print(student3.code())
print(student4.code())

print(student2.seireki_cd())
print(student3.seireki_cd())
print(student4.seireki_cd())
