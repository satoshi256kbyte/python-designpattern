"""
Adapterパターン
"""

from student import Student
from seireki_student import SeirekiStudent

student1: Student = Student(30, 'AA', 'BB')
student2: SeirekiStudent = SeirekiStudent(30, 'CC', 'DD')
student3: SeirekiStudent = SeirekiStudent(4, 'EE', 'FF')
student4: SeirekiStudent = SeirekiStudent(2023, 'GG', 'HH')
print(student1.code())
print(student2.code())
print(student3.code())
print(student4.code())

print(student2.seireki_cd())
print(student3.seireki_cd())
print(student4.seireki_cd())
