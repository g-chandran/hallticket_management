from django.urls import path, include
from .views import (
    HomepageView,
    StudentCreateView,
    ExaminerCreateView,
    StudentListView,
    ExaminerListView
)

urlpatterns = [
    path('', HomepageView.as_view(), name="home"),
    path('add-student/', StudentCreateView.as_view(), name="add-student"),
    path('add-examiner/', ExaminerCreateView.as_view(), name='add-examiner'),
    path('student/', StudentListView.as_view(), name='student-search'),
    path('examiner/', ExaminerListView.as_view(), name='examiner-search'),
]
