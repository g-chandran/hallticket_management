from django.contrib import admin
from .models import StudentProfile, ExaminerProfile, StudentExam

admin.site.register(StudentProfile)
admin.site.register(ExaminerProfile)
admin.site.register(StudentExam)