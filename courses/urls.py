from django.urls import path
from courses.views import CourseListAPIView, CourseDetailAPIView

urlpatterns = [
    path('all/', CourseListAPIView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
]