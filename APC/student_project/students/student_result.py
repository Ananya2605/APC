# Student Result

student_result = {

    "Semester 1": {
        "Maths": 85,
        "Physics": 78,
        "Programming": 90
    },

    "Semester 2": {
        "Maths": 88,
        "Chemistry": 80,
        "Data Structures": 91
    },

    "Semester 3": {
        "DBMS": 89,
        "Java": 92,
        "Computer Networks": 85
    },

    "Semester 4": {
        "Web Technology": 90,
        "Python": 94,
        "Software Engineering": 86
    },

    "Semester 5": {
        "Cloud Computing": 91,
        "AI": 89,
        "Machine Learning": 92
    },

    "Semester 6": {
        "Cyber Security": 90,
        "Big Data": 88,
        "DevOps": 93
    },

    "Semester 7": {
        "Advanced Java": 92,
        "Project": 96,
        "Elective": 89
    },

    "Semester 8": {
        "Major Project": 95,
        "Internship": 93,
        "Viva": 92
    }
}


def display_result():
    print("\n----- STUDENT RESULT -----")

    for semester, subjects in student_result.items():
        print("\n" + semester)

        for subject, marks in subjects.items():
            print(subject, ":", marks)