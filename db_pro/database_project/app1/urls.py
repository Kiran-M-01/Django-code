from . import views
from django.urls import path

urlpatterns = [
    path('students/', views.all_students),
    path('emps/',views.all_employees),
    path('one_emps/<int:id>/',views.one_employee),
    path('multiple_students/<int:n>/',views.multiple_students),
]
