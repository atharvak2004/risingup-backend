from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # New APIs (you will add as we build them)
    # path("api/accounts/", include("accounts.urls")),
    # path("api/school/", include("school.urls")),
    # path("api/students/", include("students.urls")),
    # path("api/learning/", include("learning.urls")),
    # path("api/tests/", include("tests.urls")),
]
