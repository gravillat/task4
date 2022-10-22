from django.urls import path, include
from . import views


urlpatterns = [
    path('courses-list/', views.CourseListView.as_view()),
    path('courses/<int:pk>/', views.CourseDetailCreateView.as_view())

]
