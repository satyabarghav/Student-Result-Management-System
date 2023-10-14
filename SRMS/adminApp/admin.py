from django.contrib import admin
from .models import Course,Admin,Faculty,Student,Marks,Result
# Register your models here.
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Marks)
admin.site.register(Result)