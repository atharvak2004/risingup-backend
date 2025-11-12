from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentRegistration, SchoolRegistration
from .serializers import PendingStudentSerializer, StudentSerializer, SchoolSerializer
from django.core.mail import send_mail



@api_view(["POST"])
def register_school(request):
    serializer = SchoolSerializer(data=request.data)

    if serializer.is_valid():
        school = serializer.save()

        # Send credentials to school email
        send_mail(
            subject="School Registration Successful - Login Credentials",
            message=f"""
Dear {school.schoolName},

Your school has been successfully registered 🎉

Here are your login credentials:

School ID: {school.schoolId}
Username: {school.schoolEmail}
Password: {school.password}

Login URL: https://levelup.in/login

Regards,  
LevelUp Team
""",
            from_email=None,
            recipient_list=[school.schoolEmail],
        )

        return Response(
            {
                "success": True,
                "message": "School registered successfully",
                "data": {
                    "schoolId": school.schoolId,
                    "schoolName": school.schoolName,
                }
            },
            status=201,
        )

    # ✅ Return readable serializer errors
    error_messages = {
        field: str("".join([str(err) for err in error_list]))
        for field, error_list in serializer.errors.items()
    }

    return Response(
        {
            "success": False,
            "message": "Duplicate or invalid entries found",
            "errors": error_messages
        },
        status=400,
    )



@api_view(['POST'])
def register_student(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        student = serializer.save() 

        return Response({
            "message": "Student Registered Successfully",
            "studentId": student.studentId,   
            "generatedPassword": student.password,  
        })
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def register_pending_student(request):
    serializer = PendingStudentSerializer(data=request.data)

    if serializer.is_valid():
        pending_student = serializer.save()

        return Response({
            "message": "Pending Student Registered Successfully ✅",
            "studentId": pending_student.studentId,
        }, status=201)

    return Response({
        "errors": serializer.errors,
        "message": "Validation Failed"
    }, status=400)
