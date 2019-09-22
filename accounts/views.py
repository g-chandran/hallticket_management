from django.shortcuts import render
from .models import StudentProfile, ExaminerProfile
from django.views.generic import CreateView, TemplateView, ListView
from django.db.models import Q

class HomepageView(TemplateView):
    template_name = "home.html"


class StudentCreateView(CreateView):
    model = StudentProfile
    template_name = "create.html"
    fields = [
        'rollno', 'name', 'department',
        'dob', 'address', 'mobile', 
        'email', 'year', 'image',
    ]

class ExaminerCreateView(CreateView):
    model = ExaminerProfile
    template_name = "create.html"
    fields = [
        'staffid', 'name', 'mobile',
        'email', 'address', 'image',
    ]

class StudentListView(ListView):
    model = StudentProfile
    template_name = "student_search.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = StudentProfile.objects.filter(
            Q(rollno__icontains=query)
        )
        return object_list
    

class ExaminerListView(ListView):
    model = ExaminerProfile
    template_name = 'examiner_search.html'
