from django.db import models
from django.utils.crypto import get_random_string

# ===================== SCHOOL MODEL =====================
class SchoolRegistration(models.Model):
    schoolId = models.CharField(max_length=4, unique=True, editable=False, blank=True, null=True)

    schoolName = models.CharField(max_length=150)
    schoolEmail = models.EmailField(unique=True)
    schoolContact = models.CharField(max_length=15)
    schoolAddress = models.TextField()
    schoolWebsite = models.URLField(blank=True, null=True)
    schoolAffiliation = models.CharField(max_length=20)
    schoolTrust = models.CharField(max_length=100)
    schoolGstNumber = models.CharField(max_length=20, blank=True, null=True)
    schoolPrincipalName = models.CharField(max_length=100)
    schoolPrincipalContact = models.CharField(max_length=15)
    schoolPrincipalEmail = models.EmailField(unique=True)

    password = models.CharField(max_length=128, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.schoolId:
            last_id = SchoolRegistration.objects.count() + 1
            self.schoolId = str(last_id).zfill(4)

        if not self.password:
            self.password = get_random_string(length=8)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.schoolName


# ===================== STUDENT MODEL =====================
class StudentRegistration(models.Model):
    studentId = models.CharField(max_length=50, unique=True, editable=False, blank=True, null=True)

    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    school = models.ForeignKey(SchoolRegistration, on_delete=models.CASCADE, related_name="students")

    contact = models.CharField(max_length=15)
    rollNumber = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    grade = models.CharField(max_length=20)
    birthDate = models.DateField()
    address = models.TextField()

    password = models.CharField(max_length=128, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.studentId:
            initials = self.firstName.lower()
            birth_day = self.birthDate.strftime("%d")
            self.studentId = f"{initials}{birth_day}"

        if not self.password:
            self.password = get_random_string(length=8)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

# for the students whos school is not registered yet
class PendingStudentRegistration(models.Model):
    studentId = models.CharField(max_length=50, unique=True, editable=False, blank=True, null=True)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    schoolName = models.CharField(max_length=100)
    schoolAddress = models.TextField()
    schoolPrincipalName = models.CharField(max_length=100)
    schoolPrincipalContact = models.CharField(max_length=15)
    

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name