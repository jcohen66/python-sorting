from collections import defaultdict

student_grades = {
    "Jack": [80, 90],
    "Jill": [85, 95]
}


def get_grades_naive(name):
    """
    Does nothing if not found
    """
    if name in student_grades:
        return student_grades[name]


def get_grades_better(name):
    """
    Returns default [] if not found
    """
    return student_grades.get(name, [])


def get_grades_with_assignment(name):
    """
    Assigns [] if nothing is found
    Otherwise returns what is found
    """
    if name not in student_grades:
        student_grades[name] = []
        return student_grades[name]


def get_grades_with_assignment_better(name):
    """
    Assigns [] if nothing is found
    Otherwise returns what is found
    """
    return student_grades.setdefault(name, [])


def set_grades_naive(name, score):
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]

    grades.append(score)

def set_grade_better(name, score):
    grades = get_grades_with_assignment_better(name)
    grades.append(score)


student_grades = defaultdict(list, student_grades)

def set_grade_best(name, score):
    student_grades[name].append(score)

student_score = defaultdict(lambda: 70)
print(student_score["Jack"] + 10)

set_grade_best("Zeke", 90)
print(student_grades)

student_score["Jack"] += 10

print(student_score)
