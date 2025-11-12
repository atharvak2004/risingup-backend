from rest_framework import serializers
from .models import PendingStudentRegistration, StudentRegistration, SchoolRegistration

#  SCHOOL SERIALIZER
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolRegistration
        exclude = ['password'] 

# STUDENT SERIALIZER  
class StudentSerializer(serializers.ModelSerializer):
    schoolName = serializers.CharField(source="school.schoolName", read_only=True)
    class Meta:
        model = StudentRegistration
        exclude = ['password', 'studentId']
    def create(self, validated_data):
        return super().create(validated_data)
    
# PENDING STUDENT SERIALIZER
class PendingStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingStudentRegistration
        fields = '__all__'
