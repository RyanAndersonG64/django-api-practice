from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from .models import *
from .serializers import *

def get_letter_grade(obj):
    if (obj.score > 100):
        return 'F for cheating (or being an overachiever, nobody likes overachievers)'
    elif (obj.score >= 90):
        return 'A'
    elif (obj.score >= 80):
        return 'B'
    elif (obj.score >= 70):
        return 'C'
    elif (obj.score >= 60):
        return 'D'
    elif (obj.score >= 50):
        return 'F'
    elif (obj.score >= 40):
        return 'Super F'
    else:
        return 'Hobo Tier'

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSeralizer

    def destroy(self, request, pk=None):
        course = self.get_object()
        if Grade.objects.filter(course=course).exists():
            raise ValidationError({'detail': 'course has grades'})
        
        self.perform_destroy(course)
        print('DELORTED')
        return Response

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSeralizer

    def create(self, request):
        mutable_data_copy = request.data.copy()
        mutable_data_copy['name'] = f'Señor {mutable_data_copy['name']}'
        
        serializer = InstructorSeralizer(data = mutable_data_copy)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSeralizer

    def retrieve(self, request, pk=None):
        grade = Grade.objects.get(pk=pk)
        grade_serializer = GradeSeralizer(grade)
        data = grade_serializer.data
        data['letter_grade'] = get_letter_grade(grade)
        return Response(data)

    def update(self, request, pk=None):
        grade = Grade.objects.get(pk=pk)
        grade_serializer = GradeSeralizer(data = request.data)
        grade_serializer.is_valid(raise_exception=True)
        grade_serializer.save

        student = Student.objects.get(id = grade.student.id)
        if (int(request.data['score']) > 100):
            student.name = f'{student.name} the cheater'
            student.save()
        return Response(grade_serializer.data)