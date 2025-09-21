from django.contrib import admin
from courses.models import Instructor, Category, Course

admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Course)