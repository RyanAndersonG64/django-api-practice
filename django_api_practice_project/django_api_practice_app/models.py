from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.TextField()
  age = models.PositiveSmallIntegerField()
  courses = models.ManyToManyField('Course')

  def __str__(self):
    course_list = ''
    for c in self.courses.all():
      course_list += c.name + ', '
    return f'Student: {self.name}, Age: {self.age}, Courses: {course_list}'


class Instructor(models.Model):
  name = models.TextField()

  def __str__(self):
    return f'Instructor: {self.name}'
  

class Course(models.Model):
  name = models.TextField()
  instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f'Course: {self.name}'

class Grade(models.Model):
  score = models.PositiveSmallIntegerField()
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)