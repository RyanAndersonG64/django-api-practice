"""
URL configuration for django_api_practice_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework import routers

from django_api_practice_app.views import *

router = routers.DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('', include(router.urls))
]

'''
    GET
    https://the-name-of-my-website/students/
    reads a list of all students

    GET
    /students/{id}
    reads a specific student with that id

    POST
    /students/
    creates a new student

    PUT
    /studens/{id}
    update the student with that id

    
    DELETE
    /students/{id}
    deletes the student with that id
'''