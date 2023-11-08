from datetime import date

from django.db import models


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department_choices = (("CSE-Regular", "CSE(R)"), ("CSE-Honors", "CSE(H)"), ("ECE", "ECE"), ("MECH", "MECH"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=20, blank=False, choices=department_choices)
    year_choices = (("2022-23", "2022-23"), ("2023-24", "2023-24"))
    academicYear = models.CharField(max_length=20, blank=False, choices=year_choices)
    year = models.IntegerField(blank=False)
    semester_choices = (("Odd", "Odd"), ("Even", "Even"))
    semester = models.CharField(max_length=10, blank=False, choices=semester_choices)
    coursecode = models.CharField(max_length=20, blank=False)
    courseTitle = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "course_table"

    def __str__(self):
        return self.coursecode

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentId = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=20, blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)
    department_choices = (("CSE-Regular", "CSE(R)"), ("CSE-Honors", "CSE(H)"), ("ECE", "ECE"), ("MECH", "MECH"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False, choices=department_choices)
    program_choices = (("BTECH", "BTECH"), ("BE", "BE"), ("MTECH", "MTECH"), ("PHD", "PHD"))
    program = models.CharField(max_length=50, blank=False, choices=program_choices)
    year = models.IntegerField(blank=False)
    semester_choices = (("Odd", "Odd"), ("Even", "Even"))
    semester = models.CharField(max_length=10, blank=False, choices=semester_choices)
    password = models.CharField(max_length=100, blank=False, default="1234")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)
    courses = models.ManyToManyField('Course', related_name='students',default=[])

    class Meta:
        db_table = "student_table"

    def __str__(self):
        return self.fullname

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyId = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=20, blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)
    department_choices = (("CSE-Regular", "CSE(R)"), ("CSE-Honors", "CSE(H)"), ("ECE", "ECE"), ("MECH", "MECH"), ("CSIT", "CS&IT"))
    department = models.CharField(max_length=50, blank=False, choices=department_choices)
    qualification = models.CharField(max_length=50, blank=False)
    designation = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=100, blank=False, default="1234")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "faculty_table"

    def __str__(self):
        return self.fullname

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('student', 'course', 'exam_name')

    def __str__(self):
        return f"{self.student.fullname} - {self.course.coursecode} - {self.exam_name}"