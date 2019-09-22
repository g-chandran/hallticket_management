from django.urls import path, include
from .views import (
    HomepageView,
    StudentCreateView,
    ExaminerCreateView,
    StudentListView,
    ExaminerListView,
    StudentUpdateView,
    StudentDeleteView,
    ExaminerUpdateView,
    ExaminerDeleteView
)

urlpatterns = [
    path('', HomepageView.as_view(), name="home"),
    path('add-student/', StudentCreateView.as_view(), name="add-student"),
    path('add-examiner/', ExaminerCreateView.as_view(), name='add-examiner'),
    path('student/', StudentListView.as_view(), name='student-search'),
    path('examiner/', ExaminerListView.as_view(), name='examiner-search'),
    path('student/update<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('examiner/update<int:pk>/', ExaminerUpdateView.as_view(), name='examiner-update'),
    path('student/delete<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('examiner/delete<int:pk>/', ExaminerDeleteView.as_view(), name='examiner-delete'),
]
