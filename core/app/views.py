from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseListSerializer, CourseCreateSerializer


class CourseListView(APIView):
    def get(self, request):

        courses = Course.objects.all()

        serializer = CourseListSerializer(courses, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CourseCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class CourseDetailCreateView(APIView):
    def get(self, request, pk):

        course = Course.objects.get(pk=pk)

        serializer = CourseCreateSerializer(course)

        return Response(serializer.data)




