class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        print(f"Hi, I am {self.name}")


class Student(Person):
    total_students = 0

    def __init__(self, name, email, grade):
        super().__init__(name, email)

        self.__grade = grade
        self.courses = []

        Student.total_students += 1

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Grade must be between 0 and 100")

    def add_course(self, course):
        self.courses.append(course)

    def introduce(self):
        print(
            f"Hi, I am {self.name}. "
            f"I am a student and my grade is {self.grade}"
        )

    def __str__(self):
        return f"Student: {self.name} | Grade: {self.grade}"

    @classmethod
    def get_total_students(cls):
        return cls.total_students


class Teacher(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)

        self.subject = subject
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def introduce(self):
        print(
            f"Hi, I am {self.name}. "
            f"I teach {self.subject}"
        )

    def __str__(self):
        return f"Teacher: {self.name} | Subject: {self.subject}"


class Course:
    total_courses = 0

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

        Course.total_courses += 1

        teacher.add_course(self)

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.add_course(self)

            print(
                f"{student.name} enrolled in {self.name}"
            )

        else:
            print(
                f"{student.name} is already enrolled"
            )

    def show_students(self):
        print(f"\nStudents in {self.name}:")

        if len(self.students) == 0:
            print("No students enrolled")
            return

        for student in self.students:
            print(
                f"- {student.name} "
                f"(Grade: {student.grade})"
            )

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return (
            f"Course: {self.name} | "
            f"Teacher: {self.teacher.name} | "
            f"Students: {len(self.students)}"
        )


def calculate_status(grade):

    if grade >= 50:
        return "Passed"

    return "Failed"


student1 = Student(
    "Ahmed",
    "ahmed@gmail.com",
    85
)

student2 = Student(
    "Mona",
    "mona@gmail.com",
    92
)

student3 = Student(
    "Omar",
    "omar@gmail.com",
    45
)


teacher1 = Teacher(
    "Mr. Ali",
    "ali@school.com",
    "Math"
)

teacher2 = Teacher(
    "Ms. Sara",
    "sara@school.com",
    "Python"
)


math = Course(
    "Mathematics",
    teacher1
)

python_course = Course(
    "Python Programming",
    teacher2
)


math.add_student(student1)
math.add_student(student2)
math.add_student(student3)

python_course.add_student(student1)
python_course.add_student(student2)


print("\n" + "=" * 40)
print("STUDENTS")
print("=" * 40)

print(student1)
print(student2)
print(student3)


print("\n" + "=" * 40)
print("TEACHERS")
print("=" * 40)

print(teacher1)
print(teacher2)


print("\n" + "=" * 40)
print("COURSES")
print("=" * 40)

print(math)
print(python_course)


math.show_students()

python_course.show_students()


print("\n" + "=" * 40)
print("INTRODUCTIONS")
print("=" * 40)

people = [
    student1,
    student2,
    teacher1,
    teacher2
]

for person in people:
    person.introduce()


print("\n" + "=" * 40)
print("GRADE STATUS")
print("=" * 40)

print(
    student1.name,
    "->",
    calculate_status(student1.grade)
)

print(
    student2.name,
    "->",
    calculate_status(student2.grade)
)

print(
    student3.name,
    "->",
    calculate_status(student3.grade)
)


print("\n" + "=" * 40)
print("SCHOOL STATISTICS")
print("=" * 40)

print(
    "Total students:",
    Student.get_total_students()
)

print(
    "Total courses:",
    Course.total_courses
)


print("\n" + "=" * 40)
print("TESTING GRADE")
print("=" * 40)

print("Old grade:", student1.grade)

student1.grade = 95

print("New grade:", student1.grade)

student1.grade = 150


print("\n" + "=" * 40)
print("NUMBER OF STUDENTS")
print("=" * 40)

print(
    f"{math.name} has {len(math)} students"
)

print(
    f"{python_course.name} has {len(python_course)} students"
)