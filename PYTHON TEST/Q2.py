student = "name:ali, age:17, grade:B"
print(student)


student_updated = student.replace("B", "A")
print(student_updated)

student_copy = student_updated[:]
print(student_copy)

student_deleted = student_updated.replace(", grade:A", "")
print(student_deleted)

pop_student = student_updated.split(", ")
print(pop_student)
