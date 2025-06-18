from django.contrib import admin

from .models import Payment
from edu_materials.models import Course, Lesson


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payment)
