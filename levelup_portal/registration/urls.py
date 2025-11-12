from django.urls import path
from .views import register_pending_student, register_student, register_school

urlpatterns = [
    path("register/student", register_student),
    path("register/school", register_school),
    path("register/new-student", register_pending_student),
]
