from rest_framework.generics import ListAPIView, RetrieveAPIView
from courses.models import Course
from courses.serializers import CourseSerializer

class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer