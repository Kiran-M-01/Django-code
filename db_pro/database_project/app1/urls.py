from . import views
from django.urls import path

urlpatterns = [
    path('all_students/', views.all_students),
    path('all_emps/',views.all_employees),
]
