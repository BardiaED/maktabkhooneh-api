from rest_framework.generics import ListAPIView, RetrieveAPIView
from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated

class CourseListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer