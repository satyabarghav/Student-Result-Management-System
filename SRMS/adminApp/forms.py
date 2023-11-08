from django import forms
from .models import Marks, Student


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'exam_name', 'marks_obtained']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentId','fullname', 'gender', 'department', 'program', 'year', 'semester', 'email', 'contact']