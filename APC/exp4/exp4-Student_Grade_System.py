names = []
grades = []

def add_student(name, grade):
    names.append(name)
    grades.append(grade)

def update_grade(name, grade):
    if name in names:
        i = names.index(name)
        grades[i] = grade
    else:
        print("Student not found")

def remove_student(name):
    if name in names:
        i = names.index(name)
        names.pop(i)
        grades.pop(i)
    else:
        print("Student not found")

def average_grade():
    return sum(grades) / len(grades)

def extreme_grades():
    print("Highest Grade:", max(grades))
    print("Lowest Grade:", min(grades))

add_student("Ananya", 85)
add_student("Khadija", 92)
add_student("Shahu", 78)

update_grade("Khadija", 88)
remove_student("Ananya")

print("Students:", names)
print("Grades:", grades)
print("Average Grade:", average_grade())
extreme_grades()