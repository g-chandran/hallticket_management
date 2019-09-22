from .models import StudentProfile, ExaminerProfile
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q
from django.urls import reverse_lazy

class HomepageView(TemplateView):
    template_name = "home.html"


class StudentCreateView(CreateView):
    model = StudentProfile
    template_name = "create.html"
    fields = [
        'rollno', 'name', 'department',
        'year', 'dob', 'address',
        'mobile', 'email', 'image',
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
        query = self.request.GET.get('q_student')
        object_list = StudentProfile.objects.filter(
            Q(rollno__icontains=query)
        )
        return object_list


class ExaminerListView(ListView):
    model = ExaminerProfile
    template_name = "examiner_search.html"

    def get_queryset(self):
        query = self.request.GET.get('q_examiner')
        object_list = ExaminerProfile.objects.filter(
            Q(staffid__icontains=query)
        )
        return object_list
    

class StudentUpdateView(UpdateView):
    model = StudentProfile
    template_name = "student_update.html"
    fields = [
        'rollno', 'name', 'department',
        'year', 'dob', 'address',
        'mobile', 'email', 'image',
    ]


class ExaminerUpdateView(UpdateView):
    model = ExaminerProfile
    template_name = "examiner_update.html"
    fields = [
        'staffid', 'name', 'mobile',
        'email', 'address', 'image',
    ]

class ExaminerDeleteView(DeleteView):
    model = ExaminerProfile
    template_name = "examiner_delete.html"

class StudentDeleteView(DeleteView):
    model = StudentProfile
    template_name = "student_delete.html"
